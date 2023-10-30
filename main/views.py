from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse

from .models import *


class BugReportPage(TemplateView):
    template_name = 'main/bug_report.html'


class ModLaunchPage(TemplateView):
    template_name = 'main/mod_upload.html'


class DownloadPage(TemplateView):
    template_name = 'main/download.html'


class HomePage(View):
    def get(self, request):
        return HttpResponse('HomePage')


class EventsPage(ListView):
    model = Posts
    template_name = 'main/events.html'


class EventPage(DetailView):
    model = Posts
    template_name = 'main/event.html'


class ModsPage(ListView):
    model = Mods
    template_name = 'main/mods.html'


class ModPage(DetailView):
    model = Mods
    template_name = 'main/mod.html'


class UserPage(View):
    model = Users

    def get(self, request):
        return HttpResponse('UserPage')


class ServersPage(ListView):
    model = Servers
    template_name = 'main/servers.html'


class ServerPage(DetailView):
    model = Servers
    template_name = 'main/server.html'


class ShopPage(View):
    model = Products

    def get(self, request):
        return HttpResponse('ShopPage')
