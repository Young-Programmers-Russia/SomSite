import requests
from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Server


def get_server_api_data(server_ip_port):
    server_ip, _, server_port = server_ip_port.partition(':')
    response = requests.get('https://minecraft-api.com/api/ping/%s/%s/json' % (server_ip, server_port))
    server_data = response.json()
    context = {
        'version': server_data['version']['name'],
        'icon': server_data['favicon'],
        'motd': server_data['description']['text'],
        'player_count': server_data['players']
    }
    return context


# class ServersPage(ListView):
#     template_name = "servers/servers.html"
#     queryset = Server.objects.order_by('-game_version__minecraft_version')
#     context_object_name = 'servers'
#     extra_context = {'api': get_server_api_data(i) for i in [obj.ip for obj in queryset]}
#
#
# class ServerPage(DetailView):
#     template_name = "servers/server.html"
#     model = Server
#     slug_field = 'slug'
#     context_object_name = 'server'
#     extra_context = get_server_api_data(Server.objects.get().ip)


def server_list_view(request):
    servers = [Server.objects.order_by('-game_version__minecraft_version')]
    context = {
        'servers': servers,
        **{'server': i.ip for i in [server for server in servers]}
    }
    template = "servers/servers.html"
    template_name = template
    request = request
    return render(request, template_name, context)


def server_detail_view(request, slug):
    server = Server.objects.get(slug=slug)
    context = get_server_api_data(server.ip)
    context['server'] = server
    template = 'servers/server.html'
    if request.method == "GET":
        return render(
            request,
            template,
            context
        )

