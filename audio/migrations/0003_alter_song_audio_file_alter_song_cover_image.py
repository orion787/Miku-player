# Generated by Django 5.1 on 2024-08-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0002_song_audio_file_song_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='audio/default.mp3', upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]
