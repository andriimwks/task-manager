from django.urls import path
from .views import *


app_name = 'workspace'


urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('partial/projects', PartialProjects.as_view(), name='partial_projects'),
]
