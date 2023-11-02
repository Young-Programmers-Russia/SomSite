from django.contrib import admin

# Register your models here.
from .models import Product, Order, OrderProduct, Report


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"product_slug": ["product_name"]}


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Report)



