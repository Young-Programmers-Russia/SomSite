from django.contrib import admin

# Register your models here.
from .models import Products, Orders, OrderProduct, Reports


admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrderProduct)
admin.site.register(Reports)