from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Audio
from django.http import Http404


# Create your views here.


def index(request):
    latest_audio_list = Audio.objects.order_by('-name')[:5]
    context = {'latest_audio_list': latest_audio_list}
    return render(request, 'articleaudiodb/index.html', context)


def detail(request, audio_id):
    audio = get_object_or_404(Audio, pk=audio_id)
    return render(request, 'articleaudiodb/detail.html', {'audio': audio})


def file(request, audio_id):
    response = "You're looking at the file of audio %s."
    return HttpResponse(response % audio_id)
