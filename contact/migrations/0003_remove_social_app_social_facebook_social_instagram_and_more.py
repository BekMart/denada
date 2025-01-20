# Generated by Django 4.2.16 on 2025-01-20 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_openingtime_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social',
            name='app',
        ),
        migrations.AddField(
            model_name='social',
            name='facebook',
            field=models.CharField(default=django.utils.timezone.now, max_length=350),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='social',
            name='instagram',
            field=models.CharField(default=django.utils.timezone.now, max_length=350),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='social',
            name='twitter',
            field=models.CharField(default=django.utils.timezone.now, max_length=350),
            preserve_default=False,
        ),
    ]
