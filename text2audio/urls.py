# assosiations urls.py

from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve
from . import views

from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'text2audio/', views.text2audio, name="TexttoAudio"),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
