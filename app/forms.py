from .models import Project,Profile,Rate
from django import forms

class NewProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['owner']
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_pic','bio']
class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        exclude=['rater','project']
