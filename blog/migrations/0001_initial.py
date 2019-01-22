# Generated by Django 2.1.5 on 2019-01-20 19:46

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
                ('total_kill', models.IntegerField(blank=True, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('prize_amount', models.IntegerField(blank=True, null=True)),
                ('paid_status', models.CharField(default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='pubg', max_length=100)),
                ('participants', models.IntegerField(blank=True, default=100)),
                ('timing', models.DateTimeField(default=datetime.datetime(2019, 1, 21, 1, 16, 34, 282613))),
                ('reg_fee', models.IntegerField(blank=True, default=0)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('team_type', models.CharField(blank=True, max_length=50)),
                ('prize_pool', models.IntegerField(blank=True, default=0)),
                ('per_kill', models.IntegerField(blank=True, default=0)),
                ('map', models.CharField(choices=[('Erangal', 'Erangal'), ('Miramar ', 'Miramar '), ('Sanhok', 'Sanhok'), ('Vikendi', 'Vikendi')], default='Erangal', max_length=20)),
                ('room_id', models.CharField(default='0', max_length=50)),
                ('room_pass', models.CharField(default='0', max_length=50)),
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
