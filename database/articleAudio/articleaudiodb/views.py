from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Audio, Document
from .forms import DocumentForm


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


def upload_file(request, audio_id):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            a = Audio.objects.get(pk=audio_id)
            a.audio_info = form.document
            a.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = DocumentForm()
    return render(request, 'articleaudiodb/detail.html', {'form': form})
