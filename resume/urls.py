from django.urls import re_path

from . import views

urlpatterns = [
    re_path("^resumes/?$", views.ResumesView.as_view(), name="resumes_url"),
    re_path("^resume/new/?$", views.NewResumeView.as_view(), name="new_resume_url"),
]
