from django.urls import path
from .views import *

app_name = 'main'


urlpatterns = [
    path('bug_report/', bug_report, name='bug_report'),
    path('', HomePage.as_view(), name='home'),
    path('individual_news/', IndividualNewsPage.as_view(), name='individual_news'),
    path('try', TryPage.as_view(), name='try'),
    path('about_us/', AboutUsPage.as_view(), name="about_us"),
    path('news/', NewsPage.as_view(), name="news"),
]
