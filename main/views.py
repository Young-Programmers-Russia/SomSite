from django.views.generic import TemplateView


class BugReportPage(TemplateView):
    template_name = "main/bug_report.html"


class DownloadPage(TemplateView):
    template_name = "main/download.html"


class IndividualNewsPage(TemplateView):
    template_name = "main/individual_news.html"


class HomePage(TemplateView):
    template_name = 'main/home.html'

