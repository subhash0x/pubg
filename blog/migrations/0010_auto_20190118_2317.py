# Generated by Django 2.1.5 on 2019-01-18 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190118_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timing',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 23, 17, 27, 696510)),
        ),
    ]