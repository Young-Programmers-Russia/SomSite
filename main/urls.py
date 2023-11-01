from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *


urlpatterns = [
    path('registration', RegistrationPage.as_view()),
    path('login', LoginPage.as_view()),
    path('account', AccountPage.as_view()),

    path('bug_report', BugReportPage.as_view()),
    path('download', DownloadPage.as_view()),

    path('mod_upload', ModUploadPage.as_view()),
    path('mods', ModsPage.as_view()),

    path('server', ServerPage.as_view()),
    path('servers', ServersPage.as_view()),

    path('fff', FFF.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
