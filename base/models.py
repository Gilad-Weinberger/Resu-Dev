from django.db import models
from accounts.models import User
import os

def university_logo_upload_path(instance, filename):
    filename, ext = os.path.splitext(filename)
    new_filename = f"logo_{instance.name}_{instance.country}{ext}"
    return os.path.join('universities', new_filename)

def resume_profile_image_upload_path(instance, filename):
    filename, ext = os.path.splitext(filename)
    new_filename = f"resume_{instance.resume_id}{ext}"
    return os.path.join('resumes', new_filename)

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.country.name}'

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} | {self.text}'

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=1000)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    start_date = models.DateField()
    is_current = models.BooleanField(default=False)
    end_date = models.DateField(null=True, blank=True)
    achievements = models.ManyToManyField(Achievement, related_name="achievements")
    just_created = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | {self.job_title} | Experience"

    def job_date(self):
        if self.is_current():
            return f'{self.start_date} - present'
        return f'{self.start_date} - {self.end_date}'

class University(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=university_logo_upload_path)

    def __str__(self):
        return f'{self.name}, {self.country.name}'

class Degree_Type(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Degree_Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Degree(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree_type = models.ForeignKey(Degree_Type, on_delete=models.CASCADE)
    degree_subjects = models.ManyToManyField(Degree_Subject, related_name="degree_subjects")
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        subjects = self.degree_subjects.values_list('name', flat=True)
        return f'{self.degree_type} | ' + ', '.join(subjects)

class Industry_Knowledge(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Tools_Technologies(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Others_Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Resume(models.Model):
    resume_id = models.CharField(max_length=30, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to=resume_profile_image_upload_path
    )
    job_title = models.CharField(max_length=1000, null=True, blank=True)
    full_name = models.CharField(max_length=1000, null=True, blank=True)
    email = models.EmailField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    address = models.ForeignKey(City, null=True, on_delete=models.SET_NULL, blank=True)
    bio = models.TextField(null=True, blank=True)
    experiences = models.ManyToManyField(Experience, related_name="experiences")
    degrees = models.ManyToManyField(Degree, related_name="degrees")
    industry_knowledge = models.ManyToManyField(Industry_Knowledge, blank=True, related_name="industry_knowledge")
    tools_technologies = models.ManyToManyField(Tools_Technologies, blank=True, related_name="tools_technologies")
    others_skills = models.ManyToManyField(Others_Skill, blank=True, related_name="others_skills")
    
    def save(self, *args, **kwargs):
        if not self.resume_id:
            last_resume = Resume.objects.order_by('-resume_id').first()
            if last_resume and last_resume.resume_id:
                last_id = int(last_resume.resume_id)
                new_id = str(last_id + 1)
            else:
                new_id = '1'
            self.resume_id = new_id
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} | {self.job_title} | {self.resume_id} | Resume'