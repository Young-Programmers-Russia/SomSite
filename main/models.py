import uuid

from django.db import models

from user.models import User


# Make shop a different app
class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=50)
    product_img = models.ImageField(default=None)
    product_descriptions = models.TextField(default=None)
    product_price = models.IntegerField(default=9999)
    product_slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField()
    order_price = models.IntegerField()

    def __str__(self):
        return str(self.order_id)+str(self.user_id)


class OrderProduct(models.Model):
    order_product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.order_product_id)+str(self.order_id)+str(self.product_id)


# Reports app
class Report(models.Model):
    report_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    report_text = models.TextField()

    def __str__(self):
        return str(self.report_id)+str(self.user_id)
