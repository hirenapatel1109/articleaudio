# Generated by Django 2.2.1 on 2019-05-30 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleaudiodb', '0005_auto_20190530_1923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document',
            new_name='docFile',
        ),
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.RemoveField(
            model_name='document',
            name='uploaded_at',
        ),
    ]
