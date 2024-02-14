from django.urls import path

from .views import *

app_name = 'mods'

urlpatterns = [
    path('mod_upload/', ModUploadPage.as_view(), name='mod_upload'),
    path('mods/', ModsPage.as_view(), name='mods'),
]
