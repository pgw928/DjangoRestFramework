# Generated by Django 3.1.2 on 2020-12-11 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipefavorite',
            old_name='recipe_id',
            new_name='recipe_num',
        ),
    ]
