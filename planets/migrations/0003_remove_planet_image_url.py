# Generated by Django 4.2.6 on 2024-02-23 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0002_planet_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planet',
            name='image_url',
        ),
    ]
