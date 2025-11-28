from django.urls import path
from .views import main, projects, partials


app_name = 'workspace'


urlpatterns = [
    path('', main.Dashboard.as_view(), name='dashboard'),

    path('projects/add', projects.AddProject.as_view(), name='add_project'),
    path('projects/edit', projects.EditProject.as_view(), name='edit_project'),

    path('partial/project-list', partials.ProjectList.as_view(), name='partial_project_list'),
]
