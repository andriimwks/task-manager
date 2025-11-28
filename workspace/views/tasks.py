from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from ..models import Project, Task
from ..forms import CreateTaskForm
from ..mixins import HtmxRequiredMixin


class CreateTask(LoginRequiredMixin, HtmxRequiredMixin, View):
    template_name = 'workspace/partials/task_list.html'

    def post(self, request, project_id: int):
        project = Project.objects.filter(pk=project_id, created_by=request.user).first()
        if not project:
            return HttpResponseNotFound('Project not found')
        
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(name=form.cleaned_data['task_name'], project=project)
            return redirect('workspace:partial_task_list', project_id=project_id)
        
        return HttpResponseBadRequest('Bad request')


class DeleteTask(LoginRequiredMixin, HtmxRequiredMixin, View):
    def delete(self, request, project_id: int, task_id: int):
        task = Task.objects.filter(pk=task_id, project__pk=project_id, project__created_by=request.user).first()
        if not task:
            return HttpResponseNotFound('Task not found')
        
        task.delete()

        return HttpResponse('Task was deleted', status=200)
