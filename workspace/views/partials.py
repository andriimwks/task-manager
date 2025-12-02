from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Project
from ..mixins import HtmxRequiredMixin, ProjectRequiredMixin


class ProjectList(LoginRequiredMixin, HtmxRequiredMixin, View):
    """Renders a partial template containing the list of projects created by the user."""

    template_name = "workspace/partials/project_list.html"

    def get(self, request):
        return render(
            request, self.template_name, {"projects": request.user.projects.all()}
        )


class TaskList(LoginRequiredMixin, HtmxRequiredMixin, ProjectRequiredMixin, View):
    """Renders a partial template containing the list of tasks belonging to the given project."""

    template_name = "workspace/partials/task_list.html"

    def get(self, request, project: Project):
        return render(request, self.template_name, {"tasks": project.tasks.all()})
