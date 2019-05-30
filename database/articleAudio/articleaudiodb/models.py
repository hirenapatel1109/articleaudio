from django.db import models
from django import forms


# Create your models here.

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
    is_valid = True

    # To represent this object as a string
    def __str__(self):
        return self.name


class UploadFileForm(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField()


class Document(models.Model):
    docFile = models.FileField(upload_to='audio/')
