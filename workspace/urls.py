from django.urls import path
from .views import main, projects, tasks, partials


app_name = 'workspace'


urlpatterns = [
    path('', main.Dashboard.as_view(), name='dashboard'),

    path('projects/create', projects.CreateProject.as_view(), name='create_project'),
    path('projects/<int:project_id>/update', projects.UpdateProject.as_view(), name='update_project'),
    path('projects/<int:project_id>/delete', projects.DeleteProject.as_view(), name='delete_project'),

    path('projects/<int:project_id>/tasks/create', tasks.CreateTask.as_view(), name='create_task'),
    path('tasks/<int:task_id>/update', tasks.UpdateTask.as_view(), name='update_task'),
    path('tasks/<int:task_id>/delete', tasks.DeleteTask.as_view(), name='delete_task'),

    path('partial/project-list', partials.ProjectList.as_view(), name='partial_project_list'),
    path('partial/task-list/<int:project_id>', partials.TaskList.as_view(), name='partial_task_list'),
]
