from django.urls import path
from .views import *

app_name = 'main'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', ListNewsView.as_view(), name="news-list"),
    path('news-detail/', DetailNewsView.as_view(), name='news-detail'),
    path('try', TryPage.as_view(), name='try'),
    path('bug_report/', bug_report, name='bug_report'),
    path('privacy/', privacy_view, name='privacy'),
    path('about_us/', AboutUsPage.as_view(), name="about_us"),
]
