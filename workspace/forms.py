from django import forms


class CreateProjectForm(forms.Form):
    """Form for creating a new project."""
    project_name = forms.CharField(max_length=255, min_length=3, required=True)


class UpdateProjectForm(forms.Form):
    """Form for editing the name of an existing project."""
    project_name = forms.CharField(max_length=255, min_length=3, required=True)


class CreateTaskForm(forms.Form):
    """Form for creating a new task."""
    task_name = forms.CharField(max_length=255, min_length=3, required=True)
