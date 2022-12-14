from django.db import models
from django.conf import settings

# Create your models here.


class Resume(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="resumes", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    resume = models.ForeignKey("Resume", related_name="education", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.school


class Employment(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    employment_descriptions = models.ForeignKey("JobDescriptions", related_name="employer", on_delete=models.CASCADE, null=True)
    resume = models.ForeignKey("Resume", related_name="employment", on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.company


class Projects(models.Model):
    project_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    project_descriptions = models.ForeignKey("ProjDescriptions", related_name="projects", on_delete=models.CASCADE, null=True)
    resume = models.ForeignKey("Resume", related_name="projects", on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.project_name


class Skills(models.Model):
    skills = models.CharField(max_length=200)
    resume = models.ForeignKey("Resume", related_name="skills", on_delete=models.CASCADE, null=True)


class JobDescriptions(models.Model):
    job_description = models.CharField(max_length=250)
    employment = models.ForeignKey("Employment", related_name="jobdescriptions", on_delete=models.CASCADE, null=True)


class ProjDescriptions(models.Model):
    proj_description = models.CharField(max_length=250)
    project = models.ForeignKey("Projects", related_name="projdescriptions", on_delete=models.CASCADE, null=True)
