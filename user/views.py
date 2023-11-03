from django.shortcuts import render
from django.views.generic import TemplateView
from server.models import Server


class LoginPage(TemplateView):
    template_name = "user/login.html"


class RegistrationPage(TemplateView):
    template_name = "user/registration.html"


class AccountPage(TemplateView):
    template_name = "user/account.html"
