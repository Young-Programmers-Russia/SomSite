from django.contrib import admin
from .models import Mod, Modpack, Tags


@admin.register(Mod)
class ModAdmin(admin.ModelAdmin):
    prepopulated_fields = {"mod_slug": ["mod_name"]}
    list_display = ['__str__', 'mod_link', 'show_modpacks', 'show_tags']
    list_filter = ['tags', 'modpacks']
    search_fields = ['mod_name']
    ordering = ['mod_name']

    def show_modpacks(self, obj):
        return ' || '.join([str(o) for o in obj.modpacks.all()])

    def show_tags(self, obj):
        return ' & '.join([str(i.name) for i in obj.tags.all()])


@admin.register(Modpack)
class ModpackAdmin(admin.ModelAdmin):
    list_display = ['modpack_name', 'count_mods'] 
    fields = [
        ('modpack_name', 'modpack_version'),
        'is_server',
        'minecraft_version',
        ('loader_core', 'minimal_loader_version'),
        'mods',
    ]
    filter_horizontal = ["mods"]

    def count_mods(self, obj):
        return obj.mods.all().count()


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    fields = ('name', )
