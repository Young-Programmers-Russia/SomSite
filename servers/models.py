import uuid

from django.db import models
from django.template.defaultfilters import slugify

from user.models import Users
from mods.models import Modpacks


class Server(models.Model):
    server_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    server_name = models.CharField(max_length=40)
    server_img = models.ImageField(default=None)
    server_description = models.TextField(default=None)
    server_ip = models.CharField(max_length=30)
    java_versions = models.IntegerField()
    modpack_id = models.OneToOneField(Modpacks, related_name='server_modpack_id', on_delete=models.CASCADE, null=True, blank=True)
    modpack_version = models.OneToOneField(Modpacks, related_name='server_modpack_version', on_delete=models.CASCADE, null=True, blank=True)
    minecraft_version = models.CharField(max_length=25)
    loader_core = models.CharField(max_length=50)
    minimal_loader_version = models.CharField(max_length=25)
    server_type = models.CharField(default=None, blank=True, null=True, max_length=50)
    server_slug = models.SlugField()

    def __str__(self) -> str:
        return str(self.server_name)

    def save(self, *args, **kwargs):
        if not self.server_id:
            self.server_slug = slugify(self.server_name)
        super(Server, self).save(*args, **kwargs)


class UserServer(models.Model):
    user_storage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    server_id = models.ForeignKey(Server, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()
    date_last_joined = models.DateTimeField()
    privilege = models.CharField(max_length=40)
