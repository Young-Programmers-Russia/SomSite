from django.contrib import messages
from django.contrib.auth import get_user_model, mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import RegistrationForm


class RegistrationPage(CreateView):
    model = get_user_model()
    template_name = "user/registration.html"
    form_class = RegistrationForm
    context_object_name = 'RegistrationForm '

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Enter proper information')


class AccountPage(LoginRequiredMixin, TemplateView):
    template_name = "user/account.html"
    login_url = reverse_lazy('users:login')