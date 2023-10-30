from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *


urlpatterns = [
    path('account', UserAccountPage.as_view()),
    path('login', UserLoginPage.as_view()),
    path('register', UserRegistrationPage.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
