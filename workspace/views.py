from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(TemplateView):
    template_name = 'workspace/dashboard.html'
