from typing import Iterable
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class NULL_NAMESPACE:
    bytes = b''


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(primary_key=True, max_length=25, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=25, unique=True)
    avatar = models.ImageField(null=True, blank=True)
    skin = models.ImageField(null=True, blank=True)
    somus = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_friend = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perms(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    def save(self, **kwargs):
        if not self.id:
            self.id = uuid.uuid3(NULL_NAMESPACE, "OfflinePlayer:" + self.get_username())
        return super().save(**kwargs)


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=150)
    post_img = models.ImageField()
    post_text = models.TextField()
    post_date = models.DateField()
    likes = GenericRelation(Like)

    def __str__(self) -> str:
        return str(self.post_title)

    @property
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = GenericRelation(Like)

    @property
    def total_likes(self):
        return self.likes.count()
