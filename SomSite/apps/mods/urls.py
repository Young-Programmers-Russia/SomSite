from django.urls import path

from .views import *

app_name = 'mods'

urlpatterns = [
    path('mods/upload/', ModUploadPage.as_view(), name='mod_upload'),
    path('mods/', ModsPage.as_view(), name='mods'),
]
