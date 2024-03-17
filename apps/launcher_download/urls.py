from django.urls import path

from .views import launcher_view


app_name = 'download'
urlpatterns = [
    path('', launcher_view, name='download'),
]
