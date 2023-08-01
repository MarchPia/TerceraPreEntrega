# Generated by Django 4.2.3 on 2023-08-01 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('creador', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('sinopsis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('creador', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('creador', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('sinopsis', models.TextField()),
            ],
        ),
    ]
