# Generated by Django 3.1.2 on 2020-12-11 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, null=True)),
                ('file_name', models.CharField(max_length=50, null=True)),
                ('url', models.CharField(max_length=500, null=True)),
                ('reg_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'PHOTO',
            },
        ),
        migrations.CreateModel(
            name='Refrigerator',
            fields=[
                ('fridge_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, null=True)),
                ('motion_sensor_on_off', models.IntegerField(default=0)),
                ('motion_period', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'REFRIGERATOR',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('value', models.IntegerField(blank=True, null=True)),
                ('reg_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'SENSOR',
            },
        ),
    ]
