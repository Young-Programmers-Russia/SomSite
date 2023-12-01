from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from rest_framework import views, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .forms import *
from .serializers import *


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def login_view(request, format=None):
    context = {
        'user': str(request.user),
        'auth': str(request.auth)
    }
    return Response(context)


class RegistrationPage(CreateView):
    model = get_user_model()
    template_name = "users/registration.html"
    form_class = RegistrationForm
    context_object_name = 'RegistrationForm '

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Enter proper information')

    def get_success_url(self):
        return reverse_lazy('users:login')


class AccountPage(LoginRequiredMixin, TemplateView):
    template_name = "users/account.html"
    login_url = reverse_lazy('users:login')
