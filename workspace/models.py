from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Project(models.Model):
    """Basic project model. Used primarily to separate task into \"groups\"."""

    name = models.CharField('Name', max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
