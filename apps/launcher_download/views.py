from django.views.generic import ListView
from .models import Launcher
import mimetypes
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render


class DownloadPage(ListView):
    model = Launcher
    fields = '__all__'
    template_name = 'launcher_download/download.html'
    context_object_name = 'launchers'


def download_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = 'media/downloadfile/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'launcher_download/download.html')
