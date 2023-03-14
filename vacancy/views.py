from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView

from . import models


class VacanciesView(ListView):
    model = models.Vacancy
    template_name = "vacancy/vacancies.html"


class NewVacancyView(PermissionRequiredMixin, CreateView):
    permission_required = "is_staff"
    model = models.Vacancy
    fields = ["description"]
    template_name = "vacancy/new_vacancy.html"
    success_url = reverse_lazy("menu_url")

    def handle_no_permission(self):
        return HttpResponseForbidden()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
