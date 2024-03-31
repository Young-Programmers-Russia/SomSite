from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/1', ListNewsView.as_view(), name='news-list'),
    path('news/', DetailNewsView.as_view(), name='news-detail'),
    path('privacy/', privacy_view, name='privacy'),
    path('bug_report/', bug_report, name='bug_report'),
]
