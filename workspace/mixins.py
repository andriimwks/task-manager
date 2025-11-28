from django.http import HttpResponseBadRequest
from .models import Project


class HtmxRequiredMixin:
    """Allows only handling requests that were sent by HTMX."""

    def dispatch(self, request, *args, **kwargs):
        if not request.htmx:
            return HttpResponseBadRequest('HTMX request required')
        return super().dispatch(request, *args, **kwargs)


class ProjectRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        if not project_id:
            return HttpResponseBadRequest("Project ID required")

        project = Project.objects.filter(pk=project_id, created_by=request.user).first()
        if not project_id:
            return HttpResponseBadRequest("Project not found")

        setattr(request, 'project', project)
        del kwargs['project_id']

        return super().dispatch(request, *args, **kwargs)
