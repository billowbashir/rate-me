from .models import Project,Profile
from django import forms

class NewProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['owner',]
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_pic','bio']
