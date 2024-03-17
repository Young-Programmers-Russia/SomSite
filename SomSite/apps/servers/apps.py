from django.apps import AppConfig


class ServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SomSite.apps.servers'
    verbose_name = 'servers'
