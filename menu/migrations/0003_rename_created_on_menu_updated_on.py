# Generated by Django 4.2.16 on 2025-01-15 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='created_on',
            new_name='updated_on',
        ),
    ]
