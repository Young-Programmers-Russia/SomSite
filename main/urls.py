from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view()),

    path('events', EventsPage.as_view()),
    path('event', EventPage.as_view()),

    path('mods', ModsPage.as_view()),
    path('mod', ModPage.as_view()),

    path('user', UserPage.as_view()),

    path('servers', ServersPage.as_view()),
    path('server', ServerPage.as_view()),

    path('shop', ShopPage.as_view()),
]