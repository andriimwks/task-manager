from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project


class Dashboard(TemplateView):
    template_name = 'workspace/dashboard.html'


class PartialProjects(LoginRequiredMixin, View):
    template_name = 'workspace/partials/projects.html'

    def get(self, request):
        projects = Project.objects.filter(created_by=request.user)
        return render(request, self.template_name, {'projects': projects})
