from django.contrib import admin
from .models import Mod, Modpack


class ModAdmin(admin.ModelAdmin):
    prepopulated_fields = {"mod_slug": ["mod_name"]}


admin.site.register(Mod, ModAdmin)
admin.site.register(Modpack)
