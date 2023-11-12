from django.shortcuts import render
from django.views.generic import TemplateView


class ModUploadPage(TemplateView):
    template_name = "mods/mod_upload.html"


class ModsPage(TemplateView):
    template_name = "mods/mods.html"
