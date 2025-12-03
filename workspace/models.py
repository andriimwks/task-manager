from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Project(models.Model):
    """Represents a project, which serves as a grouping for tasks."""

    name = models.CharField("Name", max_length=255)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="projects"
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Task(models.Model):
    """Represents a task associated with a specific project."""

    class Priorities(models.IntegerChoices):
        LOW = 0, "Low"
        NORMAL = 1, "Normal"
        HIGH = 2, "High"
        CRITICAL = 3, "Critical"

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField("Name", max_length=255)
    priority = models.IntegerField(
        "Priority", default=Priorities.NORMAL, choices=Priorities.choices
    )
    deadline = models.DateField("Deadline", null=True, blank=True)
    completed = models.BooleanField("Completed", default=False)

    class Meta:
        ordering = ("-priority",)
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
