import uuid

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from SomSite.apps.servers.models import Server
from SomSite.apps.users.models import CustomUser
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_slug = models.SlugField(
        max_length=50,
        unique=True
    )


# Make shop a different app
class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=50
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    img = models.ImageField(
        default=None
    )
    descriptions = models.TextField(
        default=None
    )
    price = models.IntegerField(
        default=9999
    )
    shop_slug = models.SlugField(
        max_length=50,
        unique=True,
    )
    server = models.ForeignKey(
        Server,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Orders(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT
    )
    date = models.DateField()
    status = models.BooleanField()

