from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    """Minimal user model"""

    username = None # We don't need it
    email = models.EmailField('E-mail', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Django already treats email as required

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
