# Generated by Django 3.0.6 on 2020-05-08 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='year',
        ),
    ]
