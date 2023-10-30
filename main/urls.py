from django.conf import settings
from django.conf.urls.static import static
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

    path('bug_report', BugReportPage.as_view()),
    path('mods_launch', ModLaunchPage.as_view()),
    path('download', DownloadPage.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
