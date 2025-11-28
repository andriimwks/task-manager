from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectList(LoginRequiredMixin, View):
    """Renders a partial template, displaying a list of projects created by the user."""
    template_name = 'workspace/partials/project_list.html'

    def get(self, request):
        return render(request, self.template_name, {'projects': request.user.projects.all()})
