from django.urls import path
from . import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('bug_report/', views.report_form, name='bug_report'),
    path('', HomePage.as_view(), name='home'),
    path('individual_news/', IndividualNewsPage.as_view(), name='individual_news')
]
