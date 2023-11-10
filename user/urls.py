from django.urls import path, include

from .views import *

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path(r'profile/', AccountPage.as_view(), name='account'),
    path(r'registration/', RegistrationPage.as_view(), name='registration'),
]
