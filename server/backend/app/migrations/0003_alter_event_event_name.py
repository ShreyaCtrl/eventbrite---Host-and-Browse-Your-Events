# Generated by Django 4.2.4 on 2023-08-14 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]