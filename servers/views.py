from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import Server


# Create your views here.
class ServersPage(ListView):
    template_name = "main/servers.html"
    model = Server


class ServerPage(DetailView):
    template_name = "main/server.html"
    model = Server
    slug_field = 'server_slug'
