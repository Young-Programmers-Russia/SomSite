from SomSite.servers.models import Server


def variable_to_context(request):
    return {"minecraft": Server.objects.all}