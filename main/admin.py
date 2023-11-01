from django.contrib import admin

# Register your models here.
from .models import Product, Order, OrderProduct, Report


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Report)