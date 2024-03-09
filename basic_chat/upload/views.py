from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UploadedFile
from .serializers import UploadedFileSerializer

@api_view(['POST'])
def upload_file(request):
    serializer = UploadedFileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_files(request):
    files = UploadedFile.objects.all()
    serializer = UploadedFileSerializer(files, many=True)
    return Response(serializer.data)
