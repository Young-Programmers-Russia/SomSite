from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, View
from django.shortcuts import render, redirect

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from .forms import *
from .serializers import *


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def login_view(request, format=None):
    context = {
        'user': str(request.user),
        'auth': str(request.auth),
        'template_name': "users/login.html"
    }
    return Response(context)


class RegistrationPage(CreateView):
    model = get_user_model()
    template_name = "users/registration.html"
    form_class = RegistrationForm
    context_object_name = 'RegistrationForm'

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Enter proper information')

    def get_success_url(self):
        return reverse_lazy('users:login')
    

class RegistrationView(View):
    model = get_user_model()
    template_name = "users/registration.html"
    form_class = RegistrationForm
    context_object_name = 'form'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        context = {self.context_object_name: form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    

# class LoginView(View):
#     template_name = "users/login.html"
#     form = AuthForm
#     context = None
#     success_url = "users:account"

#     def get(self, request, **kwargs):
#         kwargs.setdefault("context", self.context)
#         kwargs["form"] = self.form()
#         return render(request, self.template_name, kwargs)
    
#     def post(self, request, **kwargs):
#         if self.form.is_valid:
#             username = request.POST["username"]
#             password = request.POST["password"]
#             user = authenticate(request, username=username, password=password)
#             if user is not None and password:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse(self.success_url, kwargs={"username": username}), **kwargs)
#             else:
#                 messages.error(request, f"Wrong login credentials")
#         kwargs.setdefault("context", self.context)
#         kwargs["form"] = self.form()
#         return render(request, self.template_name, kwargs)
    

class LoginPage(LoginView):
    template_name = "users/login.html"
    next_page = "users:account"

    def form_valid(self, form):
        self.next_page = reverse(self.next_page, kwargs={"username": self.request.POST["username"]})
        return super().form_valid(form)


class PasswordChangePage(PasswordChangeView):
    success_url = "users:account"

    def form_valid(self, form) -> HttpResponse:
        self.success_url = reverse(self.success_url, kwargs={"username": self.request.user.username})
        return super().form_valid(form)


class AccountPage(View):
    template_name = "users/account.html"
    model = get_user_model().objects.all()
    context = None

    def get(self, request, username, *args, **kwargs):
        kwargs.setdefault("context", self.context)
        kwargs["abuser"] = self.model.get(username=username)
        return render(request, self.template_name, kwargs)


class LoginApiView():
    pass


class UsersApiView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    