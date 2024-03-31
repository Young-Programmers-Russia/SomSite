import uuid

from django.db import models


class Mod(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=100)
    mod_version = models.CharField(max_length=100)
    game_version = models.ForeignKey(
        'main.GameVersion',
        on_delete=models.CASCADE,
    )
    file = models.FileField()
    url = models.URLField()
    description = models.TextField()
    is_server = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return '%s' % self.name


class Modpack(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=100)
    modpack_version = models.CharField(max_length=100)
    game_version = models.ForeignKey(
        'main.GameVersion',
        on_delete=models.CASCADE,
    )
    is_server = models.BooleanField(default=False)
    mods = models.ManyToManyField(
        'Mod',
        through='ModpackMod',
        through_fields=('modpack_id', 'mod_id')
    )

    def __str__(self):
        return "%s" % self.name


class ModpackMod(models.Model):
    modpack_id = models.ForeignKey('Modpack', on_delete=models.CASCADE)
    mod_id = models.ForeignKey('Mod', on_delete=models.CASCADE)
