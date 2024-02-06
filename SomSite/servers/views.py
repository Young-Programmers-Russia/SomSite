import requests

from django.shortcuts import render

from .models import Server


def get_server_api_data(server_ip_port):
    server_ip, _, server_port = server_ip_port.partition(':')
    response = requests.get('https://minecraft-api.com/api/ping/%s/%s/json' % (server_ip, server_port))
    server_data = response.json()
    return server_data


def server_list_view(request):
    template_name = 'servers/servers.html'
    queryset = Server.objects.order_by('-game_version__minecraft_version')
    context = {'servers': queryset}
    if request.method == "GET":
        return render(request, template_name, context)


def server_detail_view(request, slug):
    server = Server.objects.get(slug=slug)
    context = get_server_api_data(server.ip)
    context['server'] = server
    template_name = 'servers/server.html'
    if request.method == "GET":
        return render(request, template_name, context)

