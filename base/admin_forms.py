from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import *

class ExperienceForm(forms.ModelForm):
    achievements = forms.ModelMultipleChoiceField(
        queryset=Achievement.objects.all(),
        widget=FilteredSelectMultiple("Achievements", is_stacked=False),
    )
    
    class Meta:
        model = Experience
        fields = '__all__'

class DegreeForm(forms.ModelForm):
    degree_subjects = forms.ModelMultipleChoiceField(
        queryset=Degree_Subject.objects.all(),
        widget=FilteredSelectMultiple("Degree Subjects", is_stacked=False),
    )

    class Meta:
        model = Degree
        fields = '__all__'

class ResumeForm(forms.ModelForm):
    experiences = forms.ModelMultipleChoiceField(
        queryset=Experience.objects.all(),
        widget=FilteredSelectMultiple("Experiences", is_stacked=False),
    )
    degrees = forms.ModelMultipleChoiceField(
        queryset=Degree.objects.all(),
        widget=FilteredSelectMultiple("Degrees", is_stacked=False),
    )
    industry_knowledge = forms.ModelMultipleChoiceField(
        queryset=Industry_Knowledge.objects.all(),
        widget=FilteredSelectMultiple("Industry Knowledge", is_stacked=False),
    )
    tools_technologies = forms.ModelMultipleChoiceField(
        queryset=Tools_Technologies.objects.all(),
        widget=FilteredSelectMultiple("Tools & Technologies", is_stacked=False),
    )
    others_skills = forms.ModelMultipleChoiceField(
        queryset=Others_Skill.objects.all(),
        widget=FilteredSelectMultiple("Others Skills", is_stacked=False),
    )

    class Meta:
        model = Resume
        fields = '__all__'
