from django.forms import ModelForm
from resumes.models import *


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = [
            "name",
            "phone",
            "email",
        ]


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "resume",
            "school",
            "degree",
            "start_date",
            "end_date",
        ]


class EmploymentForm(ModelForm):
    class Meta:
        model = Employment
        fields = [
            "resume",
            "company",
            "position",
            "start_date",
            "end_date"
        ]


class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields = [
            "resume",
            "project_name",
            "start_date",
            "end_date"
        ]


class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = [
            "resume",
            "skills"
        ]


class JobDescriptionsForm(ModelForm):
    class Meta:
        model = JobDescriptions
        fields = [
            "employment",
            "job_description",
        ]


class ProjectDescriptionsForm(ModelForm):
    class Meta:
        model = ProjDescriptions
        fields = [
            "project",
            "proj_description",
        ]
