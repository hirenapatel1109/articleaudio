from django.shortcuts import render
from django.http import HttpResponse
from .models import Audio
# Create your views here.


def index(request):
    latest_question_list = Audio.objects.order_by('-name')[:5]
    output = ', '.join([a.name for a in latest_question_list])
    return HttpResponse(output)


def detail(request, audio_id):
    return HttpResponse("You're looking at audio %s." % audio_id)


def file(request, audio_id):
    response = "You're looking at the file of audio %s."
    return HttpResponse(response % audio_id)
