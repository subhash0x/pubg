# Generated by Django 2.1.5 on 2019-01-24 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timing',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 23, 37, 29, 326980)),
        ),
    ]
