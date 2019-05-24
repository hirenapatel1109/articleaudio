from django.contrib import admin

from .models import Audio, NoAudio

# Register your models here.
admin.site.register(Audio)
admin.site.register(NoAudio)
