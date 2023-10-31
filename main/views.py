from django.views.generic import TemplateView

from .models import *


class AccountPage(TemplateView):
    template_name = "main/account.html"


class BugReportPage(TemplateView):
    template_name = "main/bug_report.html"


class DownloadPage(TemplateView):
    template_name = "main/download.html"


class LoginPage(TemplateView):
    template_name = "main/login.html"


class ModUploadPage(TemplateView):
    template_name = "main/mod_upload.html"


class ModsPage(TemplateView):
    template_name = "main/mods.html"


class RegistrationPage(TemplateView):
    template_name = "main/registration.html"


class ServerPage(TemplateView):
    template_name = "main/server.html"


class ServersPage(TemplateView):
    template_name = "main/servers.html"






