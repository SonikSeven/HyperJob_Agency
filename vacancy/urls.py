from django.urls import re_path

from . import views

urlpatterns = [
    re_path("^vacancies/?$", views.VacanciesView.as_view(), name="vacancies"),
    re_path("^vacancy/new/?$", views.NewVacancyView.as_view(), name="new_vacancy"),
]
