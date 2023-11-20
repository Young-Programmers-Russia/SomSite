from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse


def report_form(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New message: {}
        
        From:{}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['ragexzona@gmail.com'])
    return render(request, 'main/bug_report.html', {})


class IndividualNewsPage(TemplateView):
    template_name = "main/individual_news.html"


class HomePage(TemplateView):
    template_name = 'main/home.html'

