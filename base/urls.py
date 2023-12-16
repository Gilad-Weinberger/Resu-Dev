from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path('', views.dashboard, name=""),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('resume/<str:resume_id>/details', views.resume_details, name="resume_details"),
    path('resume/<str:resume_id>/bio', views.resume_bio, name="resume_bio"),
    path('resume/<str:resume_id>/experience', views.resume_experience, name="resume_experience"),
    path('resume/<str:resume_id>/education', views.resume_education, name="resume_education"),
    path('resume/<str:resume_id>/skills', views.resume_skills, name="resume_skills"),
]
