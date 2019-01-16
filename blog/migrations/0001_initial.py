# Generated by Django 2.1.5 on 2019-01-15 03:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='pubg', max_length=100)),
                ('participants', models.IntegerField(blank=True, default=100)),
                ('starts_on', models.DateField(blank=True, null=True)),
                ('timing', models.DateTimeField(default=datetime.datetime(2019, 1, 15, 9, 2, 52, 516630))),
                ('reg_fee', models.IntegerField(blank=True, default=0)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('team_type', models.CharField(blank=True, max_length=50)),
                ('prize_pool', models.IntegerField(blank=True, default=0)),
                ('per_kill', models.IntegerField(blank=True, default=0)),
                ('map', models.CharField(choices=[('Erangal', 'Erangal'), ('Miramar ', 'Miramar '), ('Sanhok', 'Sanhok'), ('Vikendi', 'Vikendi')], default='Erangal', max_length=20)),
                ('rank_1', models.IntegerField(blank=True, default=0)),
                ('rank_2', models.IntegerField(blank=True, default=0)),
                ('rank_3', models.IntegerField(blank=True, default=0)),
                ('rank_4', models.IntegerField(blank=True, default=0)),
                ('rank_5', models.IntegerField(blank=True, default=0)),
                ('rank_6', models.IntegerField(blank=True, default=0)),
                ('rank_7', models.IntegerField(blank=True, default=0)),
                ('rank_8', models.IntegerField(blank=True, default=0)),
                ('rank_9', models.IntegerField(blank=True, default=0)),
                ('rank_10', models.IntegerField(blank=True, default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_kill', models.IntegerField(blank=True, default=0)),
                ('rank', models.IntegerField(blank=True, default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='blog.Post'),
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
