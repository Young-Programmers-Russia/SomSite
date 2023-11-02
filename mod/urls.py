from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *


urlpatterns = [
    path('mod_upload/', ModUploadPage.as_view(), name='mod_upload'),
    path('mods/', ModsPage.as_view(), name='mods'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
