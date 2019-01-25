from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField( upload_to='profile_pics' , default='default.jpg')
    phone = models.CharField(max_length=10,blank=True, null=True, validators=[numeric],default='',help_text='enter your paytm no.')
    pubgusername = models.CharField(max_length=30,default='',null=True)
    User._meta.get_field('email')._unique = True
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, force_insert=False, force_update=False, using=None):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)
