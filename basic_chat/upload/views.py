from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from rest_framework import generics

class UploadFileView(generics.CreateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

class ListFilesView(generics.ListAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

class UpdateFileView(generics.UpdateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    lookup_field = 'name'  # Use the 'name' field to lookup the file

class DestroyFileView(generics.DestroyAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    lookup_field = 'name'  # Use the 'name' field to lookup the file