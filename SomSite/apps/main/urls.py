from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('report-bug/', bug_report, name='report-bug'),
    path('news', ListNewsView.as_view(), name='list-news'),
    path('news/<name>/', DetailNewsView.as_view(), name='detail-news'),
    path('privacy/', privacy_view, name='privacy')
]
