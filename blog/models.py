from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


MAP_CHOICES = (
    ('Erangal','Erangal'),
    ('Miramar ', 'Miramar '),
    ('Sanhok','Sanhok'),
    ('Vikendi','Vikendi'),
)


class Post(models.Model):
    #match_id = models.AutoField(editable=False,primary_key=True)
    title = models.CharField(max_length=100)
    participants = models.IntegerField(blank=True,default=0)
    starts_on = models.DateField(null=True, blank=True)
    reg_fee = models.IntegerField(blank=True,default=0)
    date_posted = models.DateTimeField(editable=False,default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    team_type = models.CharField(max_length=50, blank=True)
    prize_pool = models.IntegerField(blank=True,default=0)
    per_kill = models.IntegerField(blank=True,default=0)
    map = models.CharField(max_length=6, choices=MAP_CHOICES, default='Erangal')

    def __str__(self):
        return self.title
