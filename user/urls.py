from django.urls import path

from .views import *


urlpatterns = [
    path('registration/', RegistrationPage.as_view(), name='registration'),
    path('login/', LoginPage.as_view(), name='login'),
    path('account/', AccountPage.as_view(), name='account'),
]
