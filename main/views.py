from django.views.generic import TemplateView

from .models import *


class BugReportPage(TemplateView):
    template_name = "main/bug_report.html"


class DownloadPage(TemplateView):
    template_name = "main/download.html"
