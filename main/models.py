import uuid

from django.db import models


class Modpacks(models.Model):
    modpack_id = models.UUIDField(primary_key=True, default=uuid.uuid3, editable=False)
    modpack_name = models.CharField(max_length=30)
    mod_count = models.IntegerField()
    modpack_version = models.CharField(max_length=25)
    minecraft_version = models.CharField(max_length=25)
    loader_core = models.CharField(max_length=50)
    minimal_loader_version = models.CharField(max_length=25)
    is_server = models.BooleanField()


class Mods(models.Model):
    mod_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mod_name = models.CharField(max_length=30)
    mod_versions = models.CharField(max_length=30)
    mod_link = models.CharField(max_length=50)
    mod_descriptions = models.TextField()
    minecraft_versions = models.CharField(max_length=30)
    loader_core = models.CharField(max_length=50)
    minimal_loader_version = models.CharField(max_length=25)
    is_server = models.BooleanField()


class Users(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    referal_adress = models.CharField(max_length=150)
    user_img = models.ImageField()
    user_skin = models.ImageField()
    user_somus = models.IntegerField()


class Products(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=50)
    product_img = models.ImageField()
    product_descriptions = models.TextField()
    product_price = models.IntegerField()


class Servers(models.Model):
    server_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    server_name = models.CharField(max_length=40)
    server_img = models.ImageField()
    server_description = models.TextField()
    server_ip = models.CharField(max_length=30)
    java_versions = models.IntegerField()
    modpack_id = models.OneToOneField(Modpacks, on_delete=models.CASCADE)
    modpack_version = models.OneToOneField(Modpacks, on_delete=models.CASCADE)
    minecraft_version = models.CharField(max_length=25)
    loader_core = models.CharField(max_length=50)
    minimal_loader_version = models.CharField(max_length=25)
    server_type = models.CharField(default=None, blank=True, null=True)


class UserServer(models.Model):
    user_storage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    server_id = models.ForeignKey(Servers, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()
    date_last_joined = models.DateTimeField()
    privilege = models.CharField(max_length=40)


class Posts(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_img = models.ImageField()
    post_text = models.TextField()
    post_date = models.DateField()


class PostLike(models.Model):
    like_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)


class Comments(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateField()


class CommentLike(models.Model):
    like_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)


class Reports(models.Model):
    report_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    report_text = models.TextField()


class Orders(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    order_date = models.DateField()
    order_price = models.IntegerField()


class OrderProduct(models.Model):
    order_product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)


class ModModpack(models.Model):
    mod_modpack = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mod_id = models.ForeignKey(Mods, on_delete=models.CASCADE)
    modpack_id = models.ForeignKey(Modpacks, on_delete=models.CASCADE)
    minecraft_versions = models.CharField(max_length=25)
    loader_core = models.CharField(max_length=25)
    minimal_loader_versions = models.CharField(max_length=40)
