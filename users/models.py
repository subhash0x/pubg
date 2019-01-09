from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import RegexValidator

numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField( upload_to='profile_pics' , default='default.jpg')
    phone = models.CharField(max_length=10,blank=True, null=True, validators=[numeric],default='',help_text='enter your paytm no.')
    

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, force_insert=False, force_update=False, using=None):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
