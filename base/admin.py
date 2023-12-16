from django.contrib import admin
from .models import *
from .admin_forms import ExperienceForm, DegreeForm, ResumeForm

class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceForm

class DegreeAdmin(admin.ModelAdmin):
    form = DegreeForm

class ResumeAdmin(admin.ModelAdmin):
    form = ResumeForm

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Achievement)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(University)
admin.site.register(Degree_Type)
admin.site.register(Degree_Subject)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Industry_Knowledge)
admin.site.register(Tools_Technologies)
admin.site.register(Others_Skill)
admin.site.register(Resume, ResumeAdmin)