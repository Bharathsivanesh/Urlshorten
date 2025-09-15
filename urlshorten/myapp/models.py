from django.utils import timezone
from django.db import models

# Create your models here.
class Urlshorten(models.Model):
    Long_url=models.TextField()
    Short_url=models.TextField()
    Created_at = models.DateTimeField(default=timezone.now)