from django import forms


class AddProjectForm(forms.Form):
    """Form for creating a new project."""
    project_name = forms.CharField(max_length=255, min_length=3, required=True)
