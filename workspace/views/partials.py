from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from ..mixins import HtmxRequiredMixin


class ProjectList(LoginRequiredMixin, HtmxRequiredMixin, View):
    """Renders a partial template containing the list of projects created by the user."""
    template_name = 'workspace/partials/project_list.html'

    def get(self, request):
        return render(request, self.template_name, {'projects': request.user.projects.all()})
