from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = UploadedFile
        fields = ('id', 'file', 'name', 'description')
        from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('id', 'file', 'name', 'description')  # Assuming you have these fields
        extra_kwargs = {'file':{'required': False},'name': {'required': False}, 'description': {'required': False}}

