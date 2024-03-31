import requests
from typing import Any
from django.contrib import messages
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# from django.core.mail import send_mail

from .forms import ReportForm


# def report_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('full-name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#
#         data = {
#             'name': name,
#             'email': email,
#             'subject': subject,
#             'message': message
#         }
#         message = '''
#         New message: {}
#
#         From:{}
#         '''.format(data['message'], data['email'])
#         send_mail(data['subject'], message, '', ['ragexzona@gmail.com'])
#     return render(request, 'main/bug_report.html', {})


class HomeView(TemplateView):
    template_name = 'main/home.html'


class ListNewsView(TemplateView):
    template_name = 'main/news-list.html'


class DetailNewsView(TemplateView):
    template_name = "main/news-detail.html"


def bug_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, _('Спасибо за отзыв!'))
        else:
            messages.error(request, _('Пожалуйста войдите в аккаунт'))
    else:
        form = ReportForm()
    return render(request, 'main/bug_report.html', {'form': form})


class PrivacyView(TemplateView):
    template_name = "main/privacy.html"


def privacy_view(request):
    template = 'main/privacy.html'
    file = settings.STATIC_ROOT / "text" / "privacy.txt"
    f = open(file, 'r+', encoding='utf-8')
    return render(request, template, {"text": f.readlines()})
