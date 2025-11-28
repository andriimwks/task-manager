from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from ..models import Project
from ..forms import AddProjectForm,EditProjectForm
from ..mixins import HtmxRequiredMixin


class AddProject(LoginRequiredMixin, View):
    """A view for creating a new project."""

    template_name = 'workspace/add_project.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        form = AddProjectForm(request.POST)
        if form.is_valid():
            Project.objects.create(name=form.cleaned_data['project_name'], created_by=request.user)
            return redirect('workspace:dashboard')

        return render(request, self.template_name, {'form': form})


class EditProject(LoginRequiredMixin, HtmxRequiredMixin, View):
    def post(self, request):
        form = EditProjectForm(request.POST)
        if form.is_valid():
            project = Project.objects.filter(pk=form.cleaned_data['project_id'], created_by=request.user).first()
            if not project:
                return HttpResponseNotFound('Project not found')
            
            project.name = form.cleaned_data['project_name']
            project.save()

            return HttpResponse('New project name was saved', status=200)
        
        return HttpResponseBadRequest('Bad request')

