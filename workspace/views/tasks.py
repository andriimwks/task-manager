from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from ..models import Project, Task
from ..forms import CreateTaskForm
from ..mixins import HtmxRequiredMixin, ProjectRequiredMixin, TaskRequiredMixin


class CreateTask(LoginRequiredMixin, HtmxRequiredMixin, ProjectRequiredMixin, View):
    """Creates a new task within the specified project."""

    def post(self, request):       
        form = CreateTaskForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest('Bad request')

        Task.objects.create(name=form.cleaned_data['task_name'], project=request.project)
        return redirect('workspace:partial_task_list', project_id=request.project.pk)


class UpdateTask(LoginRequiredMixin, TaskRequiredMixin, View):
    """Displays a form for updating a specific task."""

    template_name = 'workspace/update_task.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                'task': request.task,
                'priority_choices': Task.Priorities.choices,
            },
        )


class DeleteTask(LoginRequiredMixin, HtmxRequiredMixin, TaskRequiredMixin, View):
    """Deletes the specified task."""

    def delete(self, request):        
        request.task.delete()
        return HttpResponse('Task was deleted', status=200)
