from django.urls import path
from .views import main, projects, partials


app_name = 'workspace'


urlpatterns = [
    path('', main.Dashboard.as_view(), name='dashboard'),

    path('projects/create', projects.CreateProject.as_view(), name='create_project'),
    path('projects/<int:id>/update', projects.UpdateProject.as_view(), name='update_project'),
    path('projects/<int:id>/delete', projects.DeleteProject.as_view(), name='delete_project'),

    path('partial/project-list', partials.ProjectList.as_view(), name='partial_project_list'),
]
