from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *


urlpatterns = [
    path('upload', ModUploadPage.as_view()),
    path('mods', ModListPage.as_view()),
    path('mods/<slug>', ModDetailPage.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
