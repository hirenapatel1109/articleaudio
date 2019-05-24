from . import views

from django.urls import path

urlpatterns = [
    # ex: /articleaudiodb/
    path('', views.index, name='index'),
    # ex: /articleaudiodb/5/
    path('<int:audio_id>/', views.detail, name='detail'),
    # ex: /articleaudiodb/5/file/
    path('<int:audio_id>/file/', views.file, name='file')
]
