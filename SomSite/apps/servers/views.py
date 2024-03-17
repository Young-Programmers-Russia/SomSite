from django.views.generic import ListView, DetailView

from .models import Server


class ServersPage(ListView):
    template_name = "servers/servers.html"
    queryset = Server.objects.order_by('-minecraft_version')
    context_object_name = 'servers'


class ServerPage(DetailView):
    template_name = "servers/server.html"
    model = Server
    slug_field = 'server_slug'
    context_object_name = 'server'

