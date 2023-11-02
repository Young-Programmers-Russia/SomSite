from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {"user_slug": ["user_name"]}


admin.site.register(User, UserAdmin)
