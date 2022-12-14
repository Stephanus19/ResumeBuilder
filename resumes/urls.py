from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("create/", create_resume, name="create_resume"),
    path("<int:id>/", show_resume, name="show_resume"),
    path("create/education", create_education, name="create_education"),
    path("create/employment", create_employment, name="create_employment"),
    path("create/project", create_project, name="create_project"),
    path("create/skills", create_skills, name="create_skills"),
    path("create/job_description", create_job_description, name="create_job_description"),
    path("create/project_description", create_project_description, name="create_project_description"),
]
