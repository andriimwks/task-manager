from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from .utils import mask_email


class User(AbstractUser):
    """Minimal user model."""

    username = None  # We don't need it
    email = models.EmailField("E-mail", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # Django already treats email as required

    objects = UserManager()

    def mask_email(self) -> str:
        """Returns a string with a partially censored local part of user's email address."""
        return mask_email(self.email)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
