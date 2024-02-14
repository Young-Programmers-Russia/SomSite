import uuid
from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Mod(models.Model):
    storage = 'mods/'
    mod_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mod_name = models.CharField(max_length=100)
    mod_versions = models.CharField(max_length=30)
    mod_link = models.CharField(max_length=300, null=True, blank=True)
    mod_file = models.FileField(upload_to=storage)
    mod_descriptions = models.TextField(default=None)
    minecraft_versions = models.CharField(max_length=30)
    loader_core = models.CharField(max_length=50)
    minimal_loader_version = models.CharField(max_length=25)
    is_server = models.BooleanField(default=False)
    mod_slug = models.SlugField(max_length=50, unique=True)
    tags = models.ManyToManyField('Tags', blank=True, null=True)

    def __str__(self):
        return self.mod_file.name.replace(self.storage, '')


class Modpack(models.Model):
    modpack_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    modpack_name = models.CharField(max_length=30)
    modpack_version = models.CharField(max_length=25)
    minecraft_version = models.CharField(max_length=25)
    loader_core = models.CharField(max_length=50)
    minimal_loader_version = models.CharField(max_length=25)
    is_server = models.BooleanField(default=False)
    mods = models.ManyToManyField('Mod', related_name='modpacks', blank=True, null=True)

    def __str__(self) -> str:
        return str(self.modpack_name)

