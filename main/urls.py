from django.urls import path

from .views import *

app_name = 'main'

urlpatterns = [
    path('bug_report/', BugReportPage.as_view(), name='bug_report'),
    path('download/', DownloadPage.as_view(), name='download'),
    path('', HomePage.as_view(), name='home'),
    path('individual_news/', IndividualNewsPage.as_view(), name='individual_news')
]
