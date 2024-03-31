from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView

from .models import Server


def get_server_api_data(server_ip_port):
    server_ip, _, server_port = server_ip_port.partition(':')
    response = requests.get('https://minecraft-api.com/api/ping/%s/%s/json' % (server_ip, server_port))
    server_data = response.json()
    return server_data


class ServersPage(ListView):
    template_name = "servers/servers.html"
    queryset = Server.objects.order_by('-minecraft_version')
    context_object_name = 'servers'


class ServerPage(DetailView):
    template_name = "servers/server.html"
    model = Server
    slug_field = 'server_slug'
    context_object_name = 'server'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        kwargs += get_server_api_data(self.model.objects.get(self.request.content_params))
        return super().get(request, *args, **kwargs)

