from django.contrib import admin
from .models import Mod, Modpack, Tags


@admin.register(Mod)
class ModAdmin(admin.ModelAdmin):
    prepopulated_fields = {"mod_slug": ["mod_name"]}
    list_display = ['__str__', 'mod_link', 'get_modpacks', 'get_tags']
    list_filter = ['tags', 'modpacks']
    search_fields = ['mod_name']
    ordering = ['mod_name']

    @admin.display(description='modpacks')
    def get_modpacks(self, obj):
        return ' & '.join([modpack.modpack_name for modpack in obj.modpacks.all()])

    @admin.display(description='tags')
    def get_tags(self, obj):
       return ' & '.join([tag.name for tag in obj.tags.all()])



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
    fields = ('name',)
    