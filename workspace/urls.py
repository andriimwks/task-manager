from django.urls import path
from .views import main, projects, partials


app_name = 'workspace'


urlpatterns = [
    path('', main.Dashboard.as_view(), name='dashboard'),
    path('add-project/', projects.AddProject.as_view(), name='add_project'),
    path('partial/projects', partials.Projects.as_view(), name='partial_projects'),
]
