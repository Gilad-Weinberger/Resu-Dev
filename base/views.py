from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .resume_forms import *
from accounts.models import User
from django.shortcuts import redirect, get_object_or_404
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def home(request):
    return render(request, 'base/home.html')

@login_required
def dashboard(request):
    user = request.user
    all_resumes = Resume.objects.filter(user=user)

    context = {
        "user": user,
        "all_resumes": all_resumes
    }
    
    return render(request, 'base/dashboard.html', context)

@login_required
def resume_details(request, resume_id):
    user = request.user
    resume = get_object_or_404(Resume, resume_id=resume_id)
    now_item = 0

    if user != resume.user:
        return redirect('base:dashboard')
    
    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:resume_bio', args=[resume_id]))
    else:
        form = DetailsForm(instance=resume)
    
    context = {
        "user": user,
        'resume': resume,
        "now_item": now_item,
        "form": form,
    }
    
    return render(request, 'resume/resume_details.html', context)


@login_required
def resume_bio(request, resume_id):
    user = request.user
    resume = get_object_or_404(Resume, resume_id=resume_id)
    now_item = 1

    if user != resume.user:
        return redirect('base:dashboard')
    
    if request.method == 'POST':
        form = BioForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            if 'next' in request.POST:
                return HttpResponseRedirect(reverse('base:resume_experience', args=[resume_id]))
            elif 'back' in request.POST:
                return HttpResponseRedirect(reverse('base:resume_details', args=[resume_id]))
    else:
        form = BioForm(instance=resume)
    
    context = {
        "user": user,
        'resume': resume,
        "now_item": now_item,
        "form": form,
    }
    
    return render(request, 'resume/resume_bio.html', context)

@login_required
def resume_experience(request, resume_id):
    user = request.user
    resume = get_object_or_404(Resume, resume_id=resume_id)
    now_item = 2
    show_exp_form = False

    if user != resume.user:
        return redirect('base:dashboard')
    
    if request.method == 'POST':
        if 'save-exp' in request.POST: 
            exp_form = ExperienceCreateForm(request.POST)
            if exp_form.is_valid():
                new_experience = exp_form.save(commit=False)
                new_experience.user = user  
                new_experience.just_created = True  
                new_experience.save()
                resume.experiences.add(new_experience)
        else:
            form = ExperienceForm(request.POST, instance=resume)
            if form.is_valid():
                if 'next' in request.POST:
                    return HttpResponseRedirect(reverse('base:resume_education', args=[resume_id]))
                elif 'back' in request.POST:
                    return HttpResponseRedirect(reverse('base:resume_bio', args=[resume_id]))
    
    form = ExperienceForm(instance=resume)
    exp_form = ExperienceCreateForm()
    achiev_form = AchievementCreateForm()

    all_resume_experiences = resume.experiences.order_by(
        '-is_current',
        '-end_date',
    )

    context = {
        "user": user,
        'resume': resume,
        "now_item": now_item,
        "form": form,
        "all_experiences": all_resume_experiences,
        "exp_form": exp_form,
        "achiev_form": achiev_form,
        "show_exp_form": show_exp_form,
    }
    
    return render(request, 'resume/resume_experience.html', context)

@login_required
def resume_education(request, resume_id):
    user = request.user
    resume = get_object_or_404(Resume, resume_id=resume_id)
    now_item = 3

    if user != resume.user:
        return redirect('base:dashboard')
    
    if request.method == 'POST':
        now_item = 3
    else:
        form = DegreeForm()

    degree_form = DegreeCreateForm()

    all_resume_degrees = resume.degrees.order_by(
        '-education_year',
    )
    
    context = {
        "user": user,
        'resume': resume,
        "now_item": now_item,
        "all_degrees": all_resume_degrees,
        "form": form,
        "degree_form": degree_form
    }
    
    return render(request, 'resume/resume_education.html', context)

@login_required
def resume_skills(request, resume_id):
    user = request.user
    resume = get_object_or_404(Resume, resume_id=resume_id)
    now_item = 4

    if user != resume.user:
        return redirect('base:dashboard')
    
    context = {
        "user": user,
        'resume': resume,
        "now_item": now_item
    }
    
    return render(request, 'resume/resume_skills.html', context)