import uuid

from django.db import models
from mods.models import Modpacks
from user.models import Users


# Make shop a different app
class Products(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=50)
    product_img = models.ImageField(default=None)
    product_descriptions = models.TextField(default=None)
    product_price = models.IntegerField(default=9999)

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    order_date = models.DateField()
    order_price = models.IntegerField()

    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    order_product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Reports app
class Reports(models.Model):
    report_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    report_text = models.TextField()

    def __str__(self):
        return self.name
