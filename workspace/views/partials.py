from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Project


class Projects(LoginRequiredMixin, View):
    template_name = 'workspace/partials/projects.html'

    def get(self, request):
        projects = Project.objects.filter(created_by=request.user)
        return render(request, self.template_name, {'projects': projects})
