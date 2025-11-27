from django.db import models


class Project(models.Model):
    """Basic project model. Used primarily to separate task into \"groups\"."""

    name = models.CharField('Name', max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
