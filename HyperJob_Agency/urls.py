"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include, re_path

from . import views


urlpatterns = [
    re_path("^admin/", admin.site.urls, name="admin_url"),
    re_path("^signup/?$", views.HyperSignupView.as_view(), name="signup_url"),
    re_path("^login/?$", views.HyperLoginView.as_view(), name="login_url"),
    re_path("^logout/?$", LogoutView.as_view(), name="logout_url"),
    path("", views.Main.as_view(), name="menu_url"),
    re_path("^home/?$", views.HomeView.as_view(), name="home_url"),
    path("", include("vacancy.urls")),
    path("", include("resume.urls")),
]
