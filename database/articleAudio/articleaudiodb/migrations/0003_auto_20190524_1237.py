# Generated by Django 2.2.1 on 2019-05-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleaudiodb', '0002_audio_audio_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='name',
            field=models.CharField(default='No Name Found', max_length=200),
        ),
        migrations.AddField(
            model_name='audio',
            name='url',
            field=models.CharField(default='No URL Found', max_length=200),
        ),
    ]
