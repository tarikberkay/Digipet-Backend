# Generated by Django 4.1.5 on 2023-01-11 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0002_alter_petmodel_eating_time_alter_petmodel_pet_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='petmodel',
            name='pet_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='eating_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 19, 23, 14, 738874)),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='pet_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 19, 23, 14, 738874)),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='sleep_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 19, 23, 14, 738874)),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='water_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 19, 23, 14, 738874)),
        ),
    ]
