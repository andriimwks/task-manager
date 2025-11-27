from django.urls import path
from .views import main, partials


app_name = 'workspace'


urlpatterns = [
    path('', main.Dashboard.as_view(), name='dashboard'),
    path('partial/projects', partials.Projects.as_view(), name='partial_projects'),
]
