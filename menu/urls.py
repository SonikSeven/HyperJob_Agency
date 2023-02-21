from django.contrib.auth.views import LogoutView
from django.urls import path, re_path

from . import views


urlpatterns = [
    path("", views.Main.as_view(), name="menu"),
    re_path("^signup/?$", views.HyperSignupView.as_view(), name="signup"),
    re_path("^login/?$", views.HyperLoginView.as_view(), name="login"),
    re_path("^logout/?$", LogoutView.as_view(), name="logout"),
    re_path("^home/?$", views.HomeView.as_view(), name="home"),
]
