from django.contrib import admin

from .models import Launcher


class LauncherAdmin(admin.ModelAdmin):
    list_filter = ['os', 'version']
    list_display = ['name', 'version', 'os']


admin.site.register(Launcher, LauncherAdmin)
