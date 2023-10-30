from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView


class ModUploadPage(TemplateView):
    template_name = 'mods/mods_upload.html'
    pass


class ModListPage(ListView):
    template_name = 'mods/mods_list.html'
    pass


class ModDetailPage(DetailView):
    template_name = 'mods/mods_detail.html'
    pass
# Create your views here.
