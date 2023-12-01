from django.contrib import admin
from .models import *


class ModpackModInline(admin.TabularInline):
    model = ModpackMod


@admin.register(Mod)
class ModAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    fields = (('name', 'mod_version'), 'game_version', ('file', 'url'), 'description', 'is_server', 'slug')
    inlines = [ModpackModInline]


@admin.register(Modpack)
class ModpackAdmin(admin.ModelAdmin):
    list_display = ['name',]
    inlines = [ModpackModInline]

