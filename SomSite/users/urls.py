from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views


app_name = 'users'
urlpatterns = [
    path('registration/', views.RegistrationPage.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('users:account')), name='password_change'),
    path('<username>', views.AccountPage.as_view(), name='account'),
]
