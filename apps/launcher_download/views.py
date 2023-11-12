from django.views.generic import ListView
from .models import Launcher

import os
from django.conf import settings
from django.http import HttpResponse, Http404


class DownloadPage(ListView):
    model = Launcher
    fields = '__all__'
    template_name = 'launcher_download/download.html'
    context_object_name = 'launchers'
