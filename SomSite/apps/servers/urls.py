from django.urls import path

from .views import *


urlpatterns = [
    path('servers/<slug:slug>/', ServerDetailView.as_view(), name='server'),
    path('servers', ServerListView.as_view(), name='servers'),
]
