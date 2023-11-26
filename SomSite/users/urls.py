from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *


app_name = 'users'
urlpatterns = [
    path('registration/', RegistrationPage.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('users:account')), name='password_change'),
    path('profile/', AccountPage.as_view(), name='account'),
]
