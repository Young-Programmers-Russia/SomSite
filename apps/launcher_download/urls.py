from django.urls import path

from . import views


app_name = 'download'
urlpatterns = [
    # path('', views.DownloadPage.as_view(), name='download'),
    path('', views.LauncherView.as_view(), name='download'),
    path('<id>', views.launcher_download, name='download_file')
]
