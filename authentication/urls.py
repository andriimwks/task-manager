from django.urls import path
from .views import RedirectToLoginPage


urlpatterns = [
    path("", RedirectToLoginPage.as_view()),
]
