from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import *


class HomePage(View):
    def get(self, request):
        return HttpResponse('HomePage')


class EventsPage(ListView):
    model = Posts
    template_name = 'main/html/events.html'


class EventPage(DetailView):
    model = Posts
    template_name = 'main/html/event.html'


class ModsPage(ListView):
    model = Mods
    template_name = 'main/html/mods.html'


class ModPage(DetailView):
    model = Mods
    template_name = 'main/html/mod.html'


class UserPage(View):
    model = Users

    def get(self, request):
        return HttpResponse('UserPage')


class ServersPage(ListView):
    model = Servers
    template_name = 'main/html/servers.html'


class ServerPage(DetailView):
    model = Servers
    template_name = 'main/html/server.html'


class ShopPage(View):
    model = Products

    def get(self, request):
        return HttpResponse('ShopPage')
