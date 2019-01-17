from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime


MAP_CHOICES = (
    ('Erangal','Erangal'),
    ('Miramar ', 'Miramar '),
    ('Sanhok','Sanhok'),
    ('Vikendi','Vikendi'),
)

# class prize(models.Model):
#     name = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_kill = models.IntegerField(blank=True,default=0)
#     rank = models.IntegerField(blank=True,default=0)

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='orders')
    payment_status = models.CharField(max_length=20, default='pending')
    total_kill = models.IntegerField(blank=True,null=True)
    rank = models.IntegerField(blank=True,null=True)
    prize_amount = models.IntegerField(blank=True,null=True)
    paid_status =  models.CharField(max_length=20, default='pending')

class Post(models.Model):
    title = models.CharField(max_length=100,default='pubg')
    participants = models.IntegerField(blank=True,default=100)
    timing = models.DateTimeField(default=datetime.now())
    reg_fee = models.IntegerField(blank=True,default=0)
    date_posted = models.DateTimeField(editable=False,default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    team_type = models.CharField(max_length=50, blank=True)
    prize_pool = models.IntegerField(blank=True,default=0)
    per_kill = models.IntegerField(blank=True,default=0)
    map = models.CharField(max_length=20, choices=MAP_CHOICES, default='Erangal')
    rank_1 = models.IntegerField(blank=True,default=0)
    rank_2 = models.IntegerField(blank=True,default=0)
    rank_3 = models.IntegerField(blank=True,default=0)
    rank_4 = models.IntegerField(blank=True,default=0)
    rank_5 = models.IntegerField(blank=True,default=0)
    rank_6 = models.IntegerField(blank=True,default=0)
    rank_7 = models.IntegerField(blank=True,default=0)
    rank_8 = models.IntegerField(blank=True,default=0)
    rank_9 = models.IntegerField(blank=True,default=0)
    rank_10 = models.IntegerField(blank=True,default=0)

    def get_successful_orders(self):
        return self.orders.filter(payment_status='TXN_SUCCESS')
        # game.orders.filter(owner=request.user).order_by('-rank')



    def __str__(self):
        return self.title
