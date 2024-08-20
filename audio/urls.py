from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('all/', views.all, name= 'all_audio'),
    path('selector/', views.song_selector_view, name = 'song_selector_view'),
    path('selector/action', views.song_selector_action, name = 'song_selector_action'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
    path('song/<int:song_id>/next/', views.play_next_song, name='play_next'),
    path('song/<int:song_id>/previous/', views.play_previous_song, name='play_previous'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)