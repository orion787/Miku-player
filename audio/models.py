from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50, blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    audio_file = models.FileField(upload_to='audio/', default='audio/default.mp3')
    lyrics = models.TextField(blank=True, null=True)
    translation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"
# Create your models here.
