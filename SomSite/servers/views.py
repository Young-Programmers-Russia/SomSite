import requests
from django.shortcuts import render

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


def get_server_data(request):
    response = requests.get('https://api.mcsrvstat.us/3/45.156.26.139')
    context = {'server_data': response.json()}
    return render(request, 'servers/server1.html', context)



