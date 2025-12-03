from django import forms


class CreateProjectForm(forms.Form):
    """Form for creating a new project."""

    project_name = forms.CharField(
        label="Name", max_length=255, min_length=3, required=True
    )


class UpdateProjectForm(forms.Form):
    """Form for editing the name of an existing project."""

    project_name = forms.CharField(
        label="Name", max_length=255, min_length=3, required=True
    )


class CreateTaskForm(forms.Form):
    """Form for creating a new task."""

    task_name = forms.CharField(
        label="Name", max_length=255, min_length=3, required=True
    )


class UpdateTaskForm(forms.Form):
    """Form for editing an existing task."""

    task_name = forms.CharField(
        label="Name", max_length=255, min_length=3, required=True
    )
    priority = forms.IntegerField(label="Priority", required=True)
    deadline = forms.DateField(label="Deadline", required=False)
    completed = forms.BooleanField(label="Completed", required=False)


class CompleteTaskForm(forms.Form):
    """Form for marking task is completed"""

    completed = forms.BooleanField(label="Completed", required=False)
