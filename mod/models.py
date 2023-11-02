import uuid
from django.db import models


class Mod(models.Model):
    mod_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mod_name = models.CharField(max_length=30)
    mod_versions = models.CharField(max_length=30)
    mod_link = models.CharField(max_length=50)
    mod_descriptions = models.TextField(default=None)
    minecraft_versions = models.CharField(max_length=30)
    loader_core = models.CharField(max_length=50)
    minimal_loader_version = models.CharField(max_length=25)
    is_server = models.BooleanField(default=False)
    mod_slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return str(self.mod_name)


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


class ModModpack(models.Model):
    mod_modpack_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mod_id = models.ForeignKey(Mod, on_delete=models.CASCADE)
    modpack_id = models.ForeignKey(Modpack, on_delete=models.CASCADE)
    minecraft_versions = models.CharField(max_length=25)
    loader_core = models.CharField(max_length=25)
    minimal_loader_versions = models.CharField(max_length=40)
