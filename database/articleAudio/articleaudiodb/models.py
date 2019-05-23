from django.db import models

# Create your models here.
from django.db import models


class NoAudio(models.Model):
    result_text = "File Not Found"


class Audio(models.Model):
    result_text = "File found"
    audio_info = ""
