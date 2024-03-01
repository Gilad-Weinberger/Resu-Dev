from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import *
from accounts.models import *

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('profile_image', 'job_title', 'full_name', 'email', 'phone', 'address')

class BioForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('bio',)

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('experiences',)

class ExperienceCreateForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

class AchievementCreateForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ('text',)

class DegreeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('degrees',)

class DegreeCreateForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = '__all__'