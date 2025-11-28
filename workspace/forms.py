from django import forms


class AddProjectForm(forms.Form):
    """Form for creating a new project."""
    project_name = forms.CharField(max_length=255, min_length=3, required=True)


class EditProjectForm(forms.Form):
    """Form for editing a name of an existing project."""
    project_id = forms.IntegerField(required=True)
    project_name = forms.CharField(max_length=255, min_length=3, required=True)


class DeleteProjectForm(forms.Form):
    """Form for deleting an existing project."""
    project_id = forms.IntegerField(required=True)
