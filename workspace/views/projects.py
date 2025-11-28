from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django_htmx.http import push_url


class AddProject(LoginRequiredMixin, View):
    template_name = 'workspace/add_project.html'

    def get(self, request):
        response = render(request, self.template_name)
        return push_url(response, reverse('workspace:add_project'))
