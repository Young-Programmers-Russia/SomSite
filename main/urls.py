from django.urls import path

from .views import *


urlpatterns = [
    path('bug_report/', BugReportPage.as_view(), name='bug_report'),
    path('download/', DownloadPage.as_view(), name='download'),
]
