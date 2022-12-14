from django.shortcuts import render, redirect, get_object_or_404
from resumes.models import *
from django.contrib.auth.decorators import login_required
from resumes.forms import *


@login_required
def home(request):
    resume_list = Resume.objects.filter(author=request.user)
    context = {"resume_list": resume_list}
    return render(request, "resumes/home.html", context)


@login_required
def show_resume(request, id):
    resume = get_object_or_404(Resume, id=id)
    context = {"resume_object": resume}
    return render(request, 'resumes/detail.html', context)


@login_required
def create_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(False)
            resume.author = request.user
            resume.save()
            return redirect("home")
    else:
        form = ResumeForm()
    context = {"form": form}
    return render(request, "resumes/create_resume.html", context)


@login_required
def create_education(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_resume")
    else:
        form = EducationForm()
    context = {"form": form}
    return render(request, "resumes/create_education.html", context)


@login_required
def create_employment(request):
    if request.method == "POST":
        form = EmploymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_resume")
    else:
        form = EmploymentForm()
    context = {"form": form}
    return render(request, "resumes/create_employment.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_resume")
    else:
        form = ProjectsForm()
    context = {"form": form}
    return render(request, "resumes/create_project.html", context)


@login_required
def create_skills(request):
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_resume")
    else:
        form = SkillsForm()
    context = {"form": form}
    return render(request, "resumes/create_skills.html", context)


@login_required
def create_job_description(request):
    if request.method == "POST":
        form = JobDescriptionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_resume")
    else:
        form = JobDescriptionsForm()
    context = {"form": form}
    return render(request, "resumes/create_job_description.html", context)


@login_required
def create_project_description(request):
    if request.method == "POST":
        form = ProjectDescriptionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_resume")
    else:
        form = ProjectDescriptionsForm()
    context = {"form": form}
    return render(request, "resumes/create_project_description.html", context)
