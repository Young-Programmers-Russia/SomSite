from django.contrib import admin

from .models import Server


class ServerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"server_slug": ["server_name"]}


admin.site.register(Server, ServerAdmin)

