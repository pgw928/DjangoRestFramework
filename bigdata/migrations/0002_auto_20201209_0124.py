# Generated by Django 3.1.2 on 2020-12-08 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommrecipe',
            old_name='refri_number',
            new_name='fridge_number',
        ),
    ]
