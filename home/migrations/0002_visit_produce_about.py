# Generated by Django 4.2.16 on 2025-01-14 16:13

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('content', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('image_1', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('image_2', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('image_3', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('restaurant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_visit', to='home.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('content', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('image_1', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('image_2', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('image_3', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('restaurant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_produce', to='home.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('content', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('image_1', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('image_2', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('image_3', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('restaurant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_about', to='home.restaurant')),
            ],
        ),
    ]
