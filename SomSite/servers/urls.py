from django.urls import path

from .views import *


urlpatterns = [
    path('<slug:slug>/', server_detail_view, name='server'),
    path('', server_list_view, name='servers'),
]
