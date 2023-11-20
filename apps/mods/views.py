from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ModsFileFieldForm


class ModUploadPage(TemplateView):
    template_name = "mods/mod_upload.html"


class ModsUploadFormView(FormView):
    form_class = ModsFileFieldForm
    template_name = 'mods/mods_upload.html'
    success_url = reverse_lazy('mods:mod_upload')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data['file_field']
        for f in files:
            ...     # Сделать так, чтобы файлы создавали свои модели
            ...     # Проверить куда они грузятся. Должны грузится в папку media
        return super().form_valid(form)


class ModsPage(TemplateView):
    template_name = "mods/mods.html"
