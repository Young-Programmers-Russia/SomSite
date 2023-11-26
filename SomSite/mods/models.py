import uuid

from django.contrib.admin import TabularInline
from django.db import models


class Modpack(models.Model):
    modpack_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    modpack_name = models.CharField(max_length=30)
    mod_count = models.IntegerField(default=0)
    modpack_version = models.CharField(max_length=25)
    minecraft_version = models.CharField(max_length=25)
    loader_core = models.CharField(max_length=50)
    minimal_loader_version = models.CharField(max_length=25)
    is_server = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.modpack_name) + str(self.modpack_version)


class Mod(models.Model):
    mod_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    modpacks = models.ManyToManyField(Modpack, blank=True)
    mod_name = models.CharField(max_length=30)
    mod_versions = models.CharField(max_length=30)
    mod_link = models.CharField(max_length=50, null=True, blank=True)
    mod_file = models.FileField(upload_to='mods/')
    mod_descriptions = models.TextField(default=None)
    minecraft_versions = models.CharField(max_length=30)
    loader_core = models.CharField(max_length=50)
    minimal_loader_version = models.CharField(max_length=25)
    is_server = models.BooleanField(default=False)
    mod_slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return str(self.mod_name)

