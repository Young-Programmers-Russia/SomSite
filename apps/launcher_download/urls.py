from django.urls import path
from .views import DownloadPage


app_name = 'download'
urlpatterns = [
    path('', DownloadPage.as_view(), name='download'),
]
