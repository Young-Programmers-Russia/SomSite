from django.http import FileResponse
from django.views import generic
from .models import Launcher


# def download_file(request, filename=''):
#     if filename is False:
#         # Define the full file path
#         filepath = settings.BASE_DIR + 'media/downloadfile/' + filename
#         # Open the file for reading content
#         path = open(filepath, 'rb')
#         # Set the mime type
#         mime_type, _ = mimetypes.guess_type(filepath)
#         # Set the return value of the HttpResponse
#         response = HttpResponse(path, content_type=mime_type)
#         # Set the HTTP header for sending to browser
#         response['Content-Disposition'] = "attachment; filename=%s" % filename
#         # Return the response value
#         return response
#     else:
#         # Load the template
#         return render(request, 'launcher_download/download.html')


class LauncherView(generic.ListView):
    model = Launcher
    template_name = 'launcher_download/download.html'
    context_object_name = 'launchers'
    ordering = ['os', '-version']


def launcher_download(request, id):
    launcher = Launcher.objects.get(id=id)
    file_name = launcher.file.path
    response = FileResponse(open(file_name, 'rb'))
    return response










