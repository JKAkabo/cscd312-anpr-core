from django.db import models
import uuid


class ProcessedImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ImageField()
    plate_number = models.CharField(max_length=100)
