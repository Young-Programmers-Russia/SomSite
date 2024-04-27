from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(BugReport)
admin.site.register(GameVersion)
