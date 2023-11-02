from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *


urlpatterns = [
    path('registration/', RegistrationPage.as_view(), name='registration'),
    path('login/', LoginPage.as_view(), name='login'),
    path('account/', AccountPage.as_view(), name='account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
