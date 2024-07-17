from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"category_slug": ["name"]}


class ShopAdmin(admin.ModelAdmin):
    prepopulated_fields = {"shop_slug": ["name"]}


admin.site.register(Product, ShopAdmin)
admin.site.register(Category, CategoryAdmin)

