from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView

from . import models


class ResumesView(ListView):
    model = models.Resume
    template_name = "resume/resumes.html"


class NewResumeView(LoginRequiredMixin, CreateView):
    model = models.Resume
    fields = ["description"]
    template_name = "resume/new_resume.html"
    success_url = reverse_lazy("menu_url")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
