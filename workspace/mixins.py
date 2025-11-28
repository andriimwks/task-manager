from django.http import HttpResponseBadRequest


class HtmxRequiredMixin:
    """Allows only handling requests that were sent by HTMX."""

    def dispatch(self, request, *args, **kwargs):
        if not request.htmx:
            return HttpResponseBadRequest('HTMX request required')
        return super().dispatch(request, *args, **kwargs)
