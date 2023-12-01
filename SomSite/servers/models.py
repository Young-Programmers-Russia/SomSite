import uuid

from django.db import models
from django.conf import settings


class Server(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    icon = models.ImageField(default=None)
    description = models.TextField(default=None)
    type = models.CharField(default=None, blank=True, null=True, max_length=50)
    java_versions = models.IntegerField()
    game_version = models.ForeignKey(
        'main.GameVersion',
        on_delete=models.CASCADE,
    )
    slug = models.SlugField()

    def __str__(self) -> str:
        return str(self.name)


class UserServer(models.Model):
    user_storage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    server_id = models.ForeignKey(Server, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()
    date_last_joined = models.DateTimeField()
    privilege = models.CharField(max_length=40)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
