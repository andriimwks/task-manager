from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from ..mixins import HtmxRequiredMixin


class ProjectList(LoginRequiredMixin, HtmxRequiredMixin, View):
    """Renders a partial template containing the list of projects created by the user."""
    template_name = 'workspace/partials/project_list.html'

    def get(self, request):
        return render(request, self.template_name, {'projects': request.user.projects.all()})


class TaskList(LoginRequiredMixin, HtmxRequiredMixin, View):
    """Renders a partial template containing the list of tasks belonging to the given project."""

    template_name = 'workspace/partials/task_list.html'

    def get(self, request, project_id: int):
        project = request.user.projects.filter(pk=project_id).first()
        if not project:
            return HttpResponseNotFound('Project not found')
        
        return render(request, self.template_name, {'tasks': project.tasks.all()})
