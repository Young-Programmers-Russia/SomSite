from django.urls import path, reverse
from django.contrib.auth.views import LogoutView, PasswordChangeView

from .views import RegistrationPage, AccountPage, LoginPage, PasswordChangePage


app_name = 'users'
urlpatterns = [
    path('registration/', RegistrationPage.as_view(), name='registration'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangePage.as_view(), name='password_change'),
    path('accounts/<username>/', AccountPage.as_view(), name='account'),
]
