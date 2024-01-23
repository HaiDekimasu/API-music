from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=200)
    audio = models.FileField(upload_to='audios')