from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload-file'),
    path('files/', views.get_files, name='get-files'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)