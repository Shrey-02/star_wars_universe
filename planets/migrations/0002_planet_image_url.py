# Generated by Django 4.2.6 on 2024-02-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]