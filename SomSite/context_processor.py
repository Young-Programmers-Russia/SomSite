from server.models import Server


def add_variable_to_context(request):
    return {"minecraft": Server.objects.all}
