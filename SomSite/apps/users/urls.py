from django.urls import path, reverse
from django.contrib.auth.views import LogoutView, PasswordChangeView

from .views import *

app_name = 'users'
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="users:login"), name='logout'),
    path('password_change/', PasswordChangePage.as_view(), name='password_change'),
    path('accounts/<username>/', AccountPage.as_view(), name='account'),
    path('api/users/', UsersApiView.as_view(), name="api-users")
]
