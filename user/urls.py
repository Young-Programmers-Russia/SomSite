from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *


urlpatterns = [
    path('registration', RegistrationPage.as_view()),
    path('login', LoginPage.as_view()),
    path('account', AccountPage.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
