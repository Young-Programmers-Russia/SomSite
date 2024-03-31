from django.urls import path

from .views import *

app_name = 'servers'
urlpatterns = [
    path('servers/<slug:slug>/', server_detail_view, name='server'),
    path('servers/', server_list_view, name='servers'),
]
