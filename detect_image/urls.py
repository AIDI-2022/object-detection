from django.conf import settings
from django.views.static import serve
from django.urls import path
urlpatterns = [
    url(r'^detect_image/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]