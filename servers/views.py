from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import Server


# Create your views here.
class ServersPage(ListView):
    template_name = "servers/servers.html"
    model = Server
    ordering = "-minecraft_version"
    context_object_name = 'servers'


class ServerPage(DetailView):
    template_name = "servers/server.html"
    model = Server
    slug_field = 'server_slug'
