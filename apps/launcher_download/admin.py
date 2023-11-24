from django.contrib import admin

from .models import Launcher


@admin.register(Launcher)
class LauncherAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'version', 'os']
    ordering = ['os', '-version']
