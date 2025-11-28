from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Project
from ..forms import AddProjectForm


class AddProject(LoginRequiredMixin, View):
    template_name = 'workspace/add_project.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        form = AddProjectForm(request.POST)
        if form.is_valid():
            Project.objects.create(name=form.cleaned_data['project_name'], created_by=request.user)
            return redirect('workspace:dashboard')

        return render(request, self.template_name, {'form': form})

