# assosiations urls.py

from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve
from . import views

from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'audio2text/', views.audio2text, name="AudiotoText"),
    re_path(r'audioupload/', views.audioupload, name="AudioUpload"),
    re_path(r'audiodelete/', views.audiodelete, name="AudioDelete"),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
