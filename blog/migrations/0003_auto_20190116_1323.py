# Generated by Django 2.1.5 on 2019-01-16 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190115_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timing',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 13, 23, 4, 265174)),
        ),
    ]
