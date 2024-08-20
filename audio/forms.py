from django import forms
from django.forms import ModelForm, TextInput
from .models import Song


class SongFilterForm(forms.Form):
    artist = forms.CharField(max_length=50, required=False, label="Artist")
    title = forms.CharField(max_length=50, required=False, label="Title")
    album = forms.CharField(max_length=50, required=False, label="Album")
    sort_by = forms.ChoiceField(choices=[
        ('title', 'Title'),
        ('artist', 'Artist'),
        ('album', 'Album'),
        ('audio_file', 'Audio File')
    ], required=False, label="Sort by")

""""class SongFilterForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album']
        widgets = {
            "title": TextInput(attrs={
                "class": "song-item",
                "placeholder" : "Название песни"
            }),
            "artist": TextInput(attrs={
                "class": "song-item",
                "placeholder" : "Исполнитель"
            }),
        }
"""