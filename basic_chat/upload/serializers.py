from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = UploadedFile
        fields = ('id', 'file')
