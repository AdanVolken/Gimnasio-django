# Generated by Django 4.2.7 on 2023-11-09 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controler', '0002_alter_dia_dia'),
    ]

    operations = [
        migrations.AddField(
            model_name='dia',
            name='hora',
            field=models.TimeField(default=datetime.time(11, 50, 43, 725759)),
        ),
    ]
