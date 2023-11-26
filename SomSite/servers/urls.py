from django.urls import path

from .views import *


urlpatterns = [
    path('<slug:slug>/', ServerPage.as_view(), name='server'),
    path('', ServersPage.as_view(), name='servers'),
    path('server', get_server_data)
]
