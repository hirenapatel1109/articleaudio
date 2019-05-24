from django.db import models

# Create your models here.
from django.db import models

# Represents no audio


class NoAudio(models.Model):
    result_text = "File Not Found"

    # To represent this object as a string
    def __str__(self):
        return self.result_text

# Represents audio with a file attached to the object


class Audio(models.Model):
    result_text = "File found"
    audio_info = models.FileField(upload_to='audio/', default="File Not Found")
    name = models.CharField(max_length=200, default="No Name Found")
    url = models.CharField(max_length=200, default="No URL Found")

    # To represent this object as a string
    def __str__(self):
        return self.url
