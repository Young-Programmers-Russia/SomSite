from django.contrib import admin
from .models import Mod, Modpack
from .forms import ModsFileFieldForm


@admin.register(Mod)
class ModAdmin(admin.ModelAdmin):
    prepopulated_fields = {"mod_slug": ["mod_name"]}


admin.site.register(Modpack)
