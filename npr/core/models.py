from django.db import models
import uuid
from cloudinary.models import CloudinaryField

class ProcessedImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = CloudinaryField()
    plate_number = models.CharField(max_length=100)
