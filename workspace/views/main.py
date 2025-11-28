from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, TemplateView):
    """Displays the main workspace dashboard for the logged-in user."""
    template_name = 'workspace/dashboard.html'
