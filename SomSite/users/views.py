from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer

from .forms import RegistrationForm


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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    User = get_user_model()
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

