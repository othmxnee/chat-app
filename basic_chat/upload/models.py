from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

