from django.urls import path
from .views import *

app_name = 'main'


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('news/', NewsPage.as_view(), name="news-list"),
    path('news-detail/', IndividualNewsPage.as_view(), name='news-detail'),
    path('try', TryPage.as_view(), name='try'),
    path('bug_report/', bug_report, name='bug_report'),
    path('privacy/', privacy_view, name='privacy'),
    path('about_us/', AboutUsPage.as_view(), name="about_us"),
]
