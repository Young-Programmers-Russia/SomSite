from django.urls import path

from .views import *

app_name = 'mods'

urlpatterns = [
    # Views
    path('mod_upload/', ModUploadPage.as_view(), name='mod_upload'),
    path('mods/', ModListView.as_view(), name='mod_list_view'),

    # API endpoints
    path('api/mod/', ModListAPI.as_view(), name='mod-api-list'),
    path('api/mod/<str:pk>/', ModDetailAPI.as_view(), name='mod-api-detail'),
]
