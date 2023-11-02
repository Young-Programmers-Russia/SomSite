from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *


urlpatterns = [
    path('<slug:slug>/', ServerPage.as_view(), name='server'),
    path('', ServersPage.as_view(), name='servers'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
