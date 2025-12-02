from django.http import HttpResponseBadRequest
from .models import Project, Task


class HtmxRequiredMixin:
    """Allows only handling requests that were sent by HTMX."""

    def dispatch(self, request, *args, **kwargs):
        if not request.htmx:
            return HttpResponseBadRequest("HTMX request required")
        return super().dispatch(request, *args, **kwargs)


class ProjectRequiredMixin:
    """Ensures the request references a valid project owned by the user."""

    def dispatch(self, request, *args, **kwargs):
        project_id = kwargs.get("project_id")
        if not project_id:
            return HttpResponseBadRequest("Project ID required")

        project = Project.objects.filter(pk=project_id, created_by=request.user).first()
        if not project:
            return HttpResponseBadRequest("Project not found")

        kwargs["project"] = project
        del kwargs["project_id"]

        return super().dispatch(request, *args, **kwargs)


class TaskRequiredMixin:
    """Ensures the request references a valid task belonging to the user's project."""

    def dispatch(self, request, *args, **kwargs):
        task_id = kwargs.get("task_id")
        if not task_id:
            return HttpResponseBadRequest("Task ID required")

        task = Task.objects.filter(pk=task_id, project__created_by=request.user).first()
        if not task:
            return HttpResponseBadRequest("Task not found")

        setattr(request, "task", task)
        del kwargs["task_id"]

        return super().dispatch(request, *args, **kwargs)
