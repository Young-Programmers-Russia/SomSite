import uuid

from django.db import models

from SomSite.apps.mods.models import Modpack
from django.conf import settings


class Server(models.Model):
    server_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    server_name = models.CharField(max_length=40)
    server_img = models.ImageField(default=None, verbose_name='')
    server_description = models.TextField(default=None)
    server_ip = models.CharField(max_length=30)
    java_versions = models.IntegerField()
    modpack_id = models.ForeignKey(Modpack, related_name='server_modpack_id', on_delete=models.CASCADE, null=True, blank=True)
    minecraft_version = models.CharField(max_length=25)
    loader_core = models.CharField(max_length=50)
    minimal_loader_version = models.CharField(max_length=25)
    server_type = models.CharField(default=None, blank=True, null=True, max_length=50)
    server_slug = models.SlugField()

    def __str__(self) -> str:
        return str(self.server_name)


class UserServer(models.Model):
    user_storage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    server_id = models.ForeignKey("Server", on_delete=models.CASCADE)
    date_joined = models.DateTimeField()
    date_last_joined = models.DateTimeField()
    privilege = models.CharField(max_length=40)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
