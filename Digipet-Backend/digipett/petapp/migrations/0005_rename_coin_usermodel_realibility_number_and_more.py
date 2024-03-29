# Generated by Django 4.1.5 on 2023-01-11 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0004_alter_petmodel_eating_time_alter_petmodel_pet_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='coin',
            new_name='realibility_number',
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='eating_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 21, 11, 38, 809302)),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='pet_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 21, 11, 38, 809302)),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='sleep_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 21, 11, 38, 809302)),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='water_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 21, 11, 38, 809302)),
        ),
    ]
