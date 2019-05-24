from django.db import models

# Create your models here.
from django.db import models

# Represents no audio


class NoAudio(models.Model):
    result_text = "File Not Found"

# Represents audio with a file attached to the object


class Audio(models.Model):
    result_text = "File found"
    audio_info = models.FileField(upload_to='audio/', default="File Not Found")
    name = models.CharField
