# Generated by Django 2.1.5 on 2019-01-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190112_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='map',
            field=models.CharField(choices=[('Erangal', 'Erangal'), ('Miramar ', 'Miramar '), ('Sanhok', 'Sanhok'), ('Vikendi', 'Vikendi')], default='Erangal', max_length=20),
        ),
    ]
