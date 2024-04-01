import requests
from multiprocessing import Pool
from django.db.models.base import Model as Model
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render

from .models import Server


def get_server_api_data(server_ip_port):
    server_ip, _, server_port = server_ip_port.partition(':')
    response = requests.get(f'https://minecraft-api.com/api/query/{server_ip}/{server_port}/json').json()
    return response  


# class ServersPage(ListView):
#     template_name = "servers/servers.html"
#     queryset = Server.objects.order_by('-minecraft_version')
#     context_object_name = 'servers'


# class ServerPage(DetailView):
#     template_name = "servers/server.html"
#     model = Server
#     slug_field = 'server_slug'
#     context_object_name = 'server'

#     def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
#         get_server_api_data(self.model.objects.get(server_slug=kwargs["slug"]).server_ip)
#         return super().get(request, *args, **kwargs)
# {'HostName': 'ItsJustAGame', 'GameType': 'SMP', 'GameName': 'MINECRAFT', 'Version': '1.20.1', 'Plugins': '', 'Map': 'world', 'Players': 0, 'MaxPlayers': 30, 'HostPort': 25565, 'HostIp': '127.0.1.1', 'Software': 'Vanilla'}

class ServerListView(View):
    template_name = "servers/servers.html"
    queryset = Server.objects.order_by('-minecraft_version')
    context = dict()

    def get(self, request, *args, **kwargs):
        servers = self.queryset
        for server in servers:
            server.api = get_server_api_data(server.server_ip)
        self.context["servers"] = servers
        return render(request, self.template_name, self.context)


class ServerDetailView(View):
    template_name = "servers/server.html"
    queryset = Server.objects.all()
    context = dict()

    def get(self, request, *args, **kwargs):
        server = self.queryset.get(server_slug=kwargs["slug"])
        self.context["server"] = server
        self.context["api"] = get_server_api_data(server.server_ip)
        return render(request, self.template_name, self.context)