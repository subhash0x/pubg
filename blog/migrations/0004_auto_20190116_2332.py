# Generated by Django 2.1.5 on 2019-01-16 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190116_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prize',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='paid_status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='rank',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='total_kill',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='timing',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 23, 32, 25, 482891)),
        ),
        migrations.DeleteModel(
            name='prize',
        ),
    ]
