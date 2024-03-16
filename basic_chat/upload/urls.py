from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.UploadFileView.as_view(), name='upload-file'),
    path('files/', views.ListFilesView.as_view(), name='get-files'),
     path('files/update/<str:name>/', views.UpdateFileView.as_view(), name='update-file'),  # Update endpoint
    path('files/delete/<str:name>/', views.DestroyFileView.as_view(), name='delete-file'),  # Delete endpoint
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)