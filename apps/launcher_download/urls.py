from django.urls import path

from . import views


app_name = 'download'
urlpatterns = [
    # path('', views.DownloadPage.as_view(), name='download'),
    path('', views.download_file, name='download'),
    path('<filename>', views.download_file, name='download_file')
]
