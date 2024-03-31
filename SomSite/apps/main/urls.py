from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', ListNewsView.as_view(), name='list-news'),
    path('news/<name>', DetailNewsView.as_view(), name='detail-news'),
    path('privacy/', privacy_view, name='privacy'),
    path('bug_report/', bug_report, name='bug_report'),
]
