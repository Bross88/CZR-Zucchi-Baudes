# Generated by Django 4.1 on 2022-09-21 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='comentarios',
        ),
    ]
