# Generated by Django 2.1.5 on 2019-01-09 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190109_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='game',
            new_name='title',
        ),
    ]
