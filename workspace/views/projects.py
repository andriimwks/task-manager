from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, HttpResponse
from ..models import Project
from ..forms import CreateProjectForm, UpdateProjectForm
from ..mixins import HtmxRequiredMixin, ProjectRequiredMixin


class CreateProject(LoginRequiredMixin, View):
    """Handles creation of a new project."""

    template_name = "workspace/create_project.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = CreateProjectForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form}, status=400)

        Project.objects.create(name=form.cleaned_data["name"], created_by=request.user)
        return redirect("workspace:dashboard")


class UpdateProject(LoginRequiredMixin, HtmxRequiredMixin, ProjectRequiredMixin, View):
    """Handles editing an existing project's name via HTMX."""

    def post(self, request, project: Project):
        form = UpdateProjectForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest("Bad request")

        project.name = form.cleaned_data["name"]
        project.save()

        return HttpResponse("New project name was saved", status=200)


class DeleteProject(LoginRequiredMixin, HtmxRequiredMixin, ProjectRequiredMixin, View):
    """Handles deletion of a project via HTMX."""

    def delete(self, request, project: Project):
        project.delete()
        return HttpResponse("Project was deleted", status=200)
