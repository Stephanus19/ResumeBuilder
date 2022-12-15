from django.shortcuts import render, redirect, get_object_or_404
from resumes.models import *
from django.contrib.auth.decorators import login_required
from resumes.forms import *
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


@login_required
def home(request):
    resume_list = Resume.objects.filter(author=request.user)
    context = {"resume_list": resume_list}
    return render(request, "resumes/home.html", context)


@login_required
def show_resume(request, id):
    resume = get_object_or_404(Resume, id=id)
    context = {"resume_object": resume}
    return render(request, 'resumes/show_resume.html', context)


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
        form = EducationForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            id = form.instance.resume.id
            return redirect("show_resume", id=id)
    else:
        form = EducationForm(request.user)
    context = {"form": form}
    return render(request, "resumes/create_education.html", context)


@login_required
def create_employment(request):
    if request.method == "POST":
        form = EmploymentForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            id = form.instance.resume.id
            return redirect("show_resume", id=id)
    else:
        form = EmploymentForm(request.user)
    context = {"form": form}
    return render(request, "resumes/create_employment.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectsForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            id = form.instance.resume.id
            return redirect("show_resume", id=id)
    else:
        form = ProjectsForm(request.user)
    context = {"form": form}
    return render(request, "resumes/create_project.html", context)


@login_required
def create_skills(request):
    if request.method == "POST":
        form = SkillsForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            id = form.instance.resume.id
            return redirect("show_resume", id=id)
    else:
        form = SkillsForm(request.user,)
    context = {"form": form}
    return render(request, "resumes/create_skills.html", context)


@login_required
def create_job_description(request):
    if request.method == "POST":
        form = JobDescriptionsForm(request.POST)
        if form.is_valid():
            form.save()
            id = form.instance.employment.resume.id
            return redirect("show_resume", id=id)
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
            id = form.instance.project.resume.id
            return redirect("show_resume", id=id)
    else:
        form = ProjectDescriptionsForm()
    context = {"form": form}
    return render(request, "resumes/create_project_description.html", context)


@login_required
def delete_resume(request, id):
    resume = get_object_or_404(Resume, id=id)
    if request.method == "POST":
        resume.delete()
        return redirect("home")
    return render(request, "resumes/delete.html")


@login_required
def delete_education(request, id):
    education = get_object_or_404(Education, id=id)
    if request.method == "POST":
        id = education.resume.id
        education.delete()
        return redirect("show_resume", id=id)
    return render(request, "resumes/delete.html")


@login_required
def delete_employment(request, id):
    employment = get_object_or_404(Employment, id=id)
    if request.method == "POST":
        id = employment.resume.id
        employment.delete()
        return redirect("show_resume", id=id)
    return render(request, "resumes/delete.html")


@login_required
def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == "POST":
        id = project.resume.id
        project.delete()
        return redirect("show_resume", id=id)
    return render(request, "resumes/delete.html")


@login_required
def delete_skill(request, id):
    skill = get_object_or_404(Skill, id=id)
    if request.method == "POST":
        id = skill.resume.id
        skill.delete()
        return redirect("show_resume", id=id)
    return render(request, "resumes/delete.html")


@login_required
def delete_job_description(request, id):
    job_descr = get_object_or_404(JobDescription, id=id)
    if request.method == "POST":
        id = job_descr.employment.resume.id
        job_descr.delete()
        return redirect("show_resume", id=id)
    return render(request, "resumes/delete.html")


@login_required
def delete_project_description(request, id):
    proj_descr = get_object_or_404(ProjDescription, id=id)
    if request.method == "POST":
        id = proj_descr.project.resume.id
        proj_descr.delete()
        return redirect("show_resume", id=id)
    return render(request, "resumes/delete.html")


@login_required
def create_resume_pdf(request, id):

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    resume = get_object_or_404(Resume, id=id)

    documentTitle = "Resume.pdf"
    title = str(resume.name)
    subtitle = f"Mobile: {resume.phone} | Email: {resume.email}"

    c.setTitle(documentTitle)
    # c.drawCentredString(300, 770, title)
    # c.drawCentredString(300, 750, subtitle)
    # c.line(30, 730, 550, 730)
    lines = []

    lines.append(title)
    lines.append(subtitle)

    lines.append("Education")
    for ed in resume.education.all():
        lines.append(f"{ed.school}" + f"{ed.start_date.strftime('%b %Y')} - {ed.end_date.strftime('%b %Y')}")
        lines.append(f"{ed.degree}")

    lines.append("Employment")
    for emp in resume.employment.all():
        lines.append(f"{emp.company} | {emp.position}" + f"{emp.start_date.strftime('%b %Y')} - {emp.end_date.strftime('%b %Y')}")
        for descr in emp.jobdescriptions.all():
            lines.append(f" - {descr}")

    lines.append("Projects")
    for prj in resume.projects.all():
        lines.append(f"{prj.project_name}" + f"{prj.start_date.strftime('%b %Y')} - {prj.end_date.strftime('%b %Y')}")
        for descr in prj.projdescriptions.all():
            lines.append(f" - {descr}")

    skills_str = ""
    for sk in resume.skillset.all():
        skills_str += (str(sk.skills) + ", ")
    skills_str = skills_str[0:-2]
    lines.append("Skills: " + skills_str)

    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename="Resume.pdf")
