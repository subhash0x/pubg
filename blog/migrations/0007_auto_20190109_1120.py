# Generated by Django 2.1.5 on 2019-01-09 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190109_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='game',
        ),
    ]
