from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class Projects(LoginRequiredMixin, View):
    """Renders a partial template, displaying a list of projects created by the user."""
    template_name = 'workspace/partials/projects.html'

    def get(self, request):
        return render(request, self.template_name, {'projects': request.user.projects.all()})
