# Generated by Django 4.1 on 2022-09-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono_movil', models.CharField(blank=True, max_length=50, null=True)),
                ('pais', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('cuit', models.IntegerField(blank=True, null=True)),
                ('comentarios', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
