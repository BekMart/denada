# Generated by Django 4.2.18 on 2025-02-06 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_restaurant_num_tables'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='about',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='max_capacity',
        ),
    ]
