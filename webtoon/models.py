from django.db import models

class Episode(models.Model):
    title = models.CharField(max_length=50)
    url=models.URLField()

# Create your models here.
