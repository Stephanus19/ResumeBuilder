from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("create/", create_resume, name="create_resume")
]
