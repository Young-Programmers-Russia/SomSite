from django.shortcuts import render

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


def launcher_view(request):
    linux = Launcher.objects.filter(os="LINUX").order_by('-version')[:1]
    windows = Launcher.objects.filter(os="WINDOWS").order_by('-version')[:1]
    mac = Launcher.objects.filter(os="MAC").order_by('-version')[:1]
    context = {}
    for os_str, os in {'linux': linux, 'windows': windows, 'mac': mac}.items():
        try:
            context[os_str] = os.get()
        except Launcher.DoesNotExist:
            continue
    return render(request, 'launcher_download/download.html', context)









