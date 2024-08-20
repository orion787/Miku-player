from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Song
from .forms import SongFilterForm
import random


def song_player(request):
    song = Song.objects.first()
    return render(request, 'audio/song_player.html', {'song' : song})

def all(request):
    songs = Song.objects.all()
    return render(request, 'audio/all_audio.html', {'songs': songs})

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'audio/song_player.html', {'song': song})

def song_selector_view(request):
    if request.method == "POST":
        return redirect('song_selector_action')
    form = SongFilterForm()
    songs = Song.objects.all()
    return render(request, 'audio/selector.html', {'songs': songs, 'form': form})
    

def song_selector_action(request):
    if request.method == "POST":
        form = SongFilterForm(request.POST)
        songs = Song.objects.all()

        if form.is_valid():
            # Фильтрация по исполнителю
            artist = form.cleaned_data.get('artist')
            if artist:
                songs = songs.filter(artist__icontains=artist)

            # Фильтрация по названию
            title = form.cleaned_data.get('title')
            if title:
                songs = songs.filter(title__icontains=title)

            # Фильтрация по альбому
            album = form.cleaned_data.get('album')
            if album:
                songs = songs.filter(album__icontains=album)

            # Сортировка
            sort_by = form.cleaned_data.get('sort_by')
            if sort_by:
                songs = songs.order_by(sort_by)

            return render(request, 'audio/all_audio.html', {'songs': songs})

    return redirect('song_selector_view')



def play_next_song(request, song_id: int):
    songs = list(Song.objects.all())
    current_song = get_object_or_404(Song, pk=song_id)
    next_song = random.choice([song for song in songs if song != current_song])

    return render(request, 'audio/song_player.html', {'song': next_song})

def play_previous_song(request, song_id: int):
    songs = list(Song.objects.all())
    current_song = get_object_or_404(Song, pk=song_id)
    previous_song = random.choice([song for song in songs if song != current_song])
    return render(request, 'audio/song_player.html', {'song': previous_song})
