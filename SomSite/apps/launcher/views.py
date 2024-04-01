from django import views
from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response

from .serializers import LauncherSerializer
from .models import Launcher


os_list = ['linux', 'windows', 'mac']


class LauncherView(views.View):
    def get(self, request):
            context = dict()
            for os_str in os_list:
                try:
                    context[os_str] = Launcher.objects.filter(os=os_str).order_by('-version')[:1].get()
                except Launcher.DoesNotExist:
                    continue
            return render(request, 'launcher/download.html', context)


class LauncherApi(views.APIView):
    def get(self, request):
            context = dict()
            for os_str in os_list:
                try:
                    context[os_str] = LauncherSerializer(Launcher.objects.filter(os=os_str).order_by('-version')[:1].get(), context={'request': request}).data
                except Launcher.DoesNotExist:
                    continue
            return Response({'updates': context})
    