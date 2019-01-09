from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    Platform = models.CharField(max_length=30, blank=True)
    participants = models.IntegerField(max_length=100,blank=True,default=0)
    starts_on = models.DateField(null=True, blank=True)
    reg_fee = models.IntegerField(blank=True,default=0)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    team_type = models.CharField(max_length=50, blank=True)



    # participants = models.IntegerField(max_length=30, blank=True,default=100)
    # # starts_on = models.DateTimeField()
    # Platform = models.CharField(max_length=100)
    # reg_fee = models.IntegerField(default=0)
    # team_type = models.CharField(max_length=100)
    # participants = models.IntegerField(default=0)
    def __str__(self):
        return self.title
