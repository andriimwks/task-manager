from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, TemplateView):
    """An entry point to the workspace, which further acts as a SPA."""
    template_name = 'workspace/dashboard.html'
