from django.urls import path

from .views import *

app_name = 'download'
urlpatterns = [
    path('download/', LauncherView.as_view(), name='download'),
    path('api/launchers', LauncherApi.as_view(), name='launcher-api-lts'),
]
