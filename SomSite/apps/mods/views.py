from rest_framework import generics

from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, DetailView

from .forms import ModsFileFieldForm
from .models import Mod
from .serializers import ModSerializer


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
            Mod(mod_file=f)
        form.save()
        return super().form_valid(form)


class ModListView(ListView):
    model = Mod
    template_name = "mods/mod-list.html"
    context_object_name = 'mods'


class ModDetailView(DetailView):
    model = Mod
    template_name = "mods/mod_detail.html"


class ModListAPI(generics.ListAPIView):
    queryset = Mod.objects.all()
    serializer_class = ModSerializer


class ModDetailAPI(generics.RetrieveAPIView):
    queryset = Mod.objects.all()
    serializer_class = ModSerializer
