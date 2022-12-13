from django.shortcuts import render, redirect
from resumes.models import *
from django.contrib.auth.decorators import login_required
from resumes.forms import *


@login_required
def home(request):
    resume_list = Resume.objects.filter(author=request.user)
    context = {"resume_list": resume_list}
    return render(request, "resumes/home.html", context)


@login_required
def create_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(False)
            resume.purchaser = request.user
            resume.save()
            return redirect("home")
    else:
        form = ResumeForm()
    context = {"form": form}
    return render(request, "resumes/create_resume.html", context)
