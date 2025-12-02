from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, HttpResponse
from ..models import Project, Task
from ..forms import CreateTaskForm, UpdateTaskForm, CompleteTaskForm
from ..mixins import HtmxRequiredMixin, ProjectRequiredMixin, TaskRequiredMixin


class CreateTask(LoginRequiredMixin, HtmxRequiredMixin, ProjectRequiredMixin, View):
    """Creates a new task within the specified project."""

    def post(self, request, project: Project):
        form = CreateTaskForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest("Bad request")

        Task.objects.create(name=form.cleaned_data["task_name"], project=project)
        return redirect("workspace:partial_task_list", project_id=project.pk)


class UpdateTask(LoginRequiredMixin, TaskRequiredMixin, View):
    """Displays a form for updating a specific task."""

    template_name = "workspace/update_task.html"

    def get(self, request, task: Task):
        return render(
            request,
            self.template_name,
            {
                "task": task,
                "priority_choices": Task.Priorities.choices,
            },
        )

    def post(self, request, task: Task):
        form = UpdateTaskForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "task": task,
                    "priority_choices": Task.Priorities.choices,
                },
            )

        task.name = form.cleaned_data["task_name"]
        task.priority = form.cleaned_data["priority"]
        task.completed = form.cleaned_data["completed"]
        task.save()

        return redirect("workspace:dashboard")


class CompleteTask(LoginRequiredMixin, HtmxRequiredMixin, TaskRequiredMixin, View):
    """todo"""

    def post(self, request, task: Task):
        form = CompleteTaskForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest("Bad request")

        task.completed = form.cleaned_data["completed"]
        task.save()

        return HttpResponse("Task was completed", status=200)


class DeleteTask(LoginRequiredMixin, HtmxRequiredMixin, TaskRequiredMixin, View):
    """Deletes the specified task."""

    def delete(self, request, task: Task):
        task.delete()
        return HttpResponse("Task was deleted", status=200)
