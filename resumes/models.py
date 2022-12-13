from django.db import models
from django.conf import settings

# Create your models here.


class Resume(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="resumes", on_delete=models.CASCADE, null=True)
    education = models.ForeignKey("Education", related_name="resumes", on_delete=models.CASCADE, null=True)
    employment = models.ForeignKey("Employment", related_name="resumes", on_delete=models.CASCADE, null=True)
    projects = models.ForeignKey("Projects", related_name="resumes", on_delete=models.CASCADE, null=True)
    skills = models.ForeignKey("Skills", related_name="resumes", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()


class Employment(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    descriptions = models.ForeignKey("Descriptions", related_name="employment", on_delete=models.CASCADE, null=True)


class Projects(models.Model):
    project_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    descriptions = models.ForeignKey("Descriptions", related_name="projects", on_delete=models.CASCADE, null=True)


class Skills(models.Model):
    skills = models.CharField(max_length=200)


class Descriptions(models.Model):
    description = models.CharField(max_length=250)
