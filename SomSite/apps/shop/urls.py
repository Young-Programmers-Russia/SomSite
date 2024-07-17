from django.urls import path

from .views import *


urlpatterns = [
    path('shop/', shop_view, name='shop'),
]
