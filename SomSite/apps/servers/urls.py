from django.urls import path

from .views import *


urlpatterns = [
    path('servers/<slug:slug>/', ServerPage.as_view(), name='server'),
    path('servers', ServersPage.as_view(), name='servers'),
]
