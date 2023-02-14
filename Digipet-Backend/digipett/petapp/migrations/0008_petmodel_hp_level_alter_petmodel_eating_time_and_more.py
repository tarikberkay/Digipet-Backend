# Generated by Django 4.1.5 on 2023-01-24 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0007_alter_petmodel_eating_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='petmodel',
            name='hp_level',
            field=models.FloatField(default=10),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='eating_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 24, 13, 40, 25, 849278)),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='pet_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 24, 13, 40, 25, 849278)),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='sleep_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 24, 13, 40, 25, 849278)),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='water_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 24, 13, 40, 25, 849278)),
        ),
    ]
