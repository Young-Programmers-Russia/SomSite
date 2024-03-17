from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'users'

urlpatterns = [
    path('account/registration/', RegistrationPage.as_view(), name='registration'),
    path('account/login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('users:account')), name='password_change'),
    path('account/profile/', AccountPage.as_view(), name='account'),
    # path('', ),
]
