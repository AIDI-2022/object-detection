from django.urls import path
from django.views.generic import RedirectView
from detect_image.views import detect, yolo_detect_api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',detect),
    path('detect/', detect),
    # path('', RedirectView.as_view(url='detect/')),
    path('detect/api/', yolo_detect_api),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
