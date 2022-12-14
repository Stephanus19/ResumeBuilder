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
    descriptions = models.ForeignKey("JobDescriptions", related_name="employment", on_delete=models.CASCADE, null=True)
    resume = models.ForeignKey("Resume", related_name="employment", on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.company


class Projects(models.Model):
    project_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    descriptions = models.ForeignKey("ProjectDescriptions", related_name="projects", on_delete=models.CASCADE, null=True)
    resume = models.ForeignKey("Resume", related_name="projects", on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.project_name


class Skills(models.Model):
    skills = models.CharField(max_length=200)
    resume = models.ForeignKey("Resume", related_name="skills", on_delete=models.CASCADE, null=True)


class JobDescriptions(models.Model):
    description = models.CharField(max_length=250)
    employment = models.ForeignKey("Employment", related_name="descriptions", on_delete=models.CASCADE, null=True)


class ProjectDescriptions(models.Model):
    description = models.CharField(max_length=250)
    project = models.ForeignKey("Project", related_name="descriptions", on_delete=models.CASCADE, null=True)
