from django.shortcuts import render
from django.views.generic import TemplateView


class UserAccountPage(TemplateView):
    template_name = "user/account.html"
    pass


class UserRegistrationPage(TemplateView):
    template_name = "user/registration.html"
    pass


class UserLoginPage(TemplateView):
    template_name = "user/login.html"
    pass
