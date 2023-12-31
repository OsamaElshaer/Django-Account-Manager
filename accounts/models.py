

from django.db import models
from django.contrib.auth.models import User , AbstractUser , AbstractBaseUser,PermissionsMixin
from django.core.validators import MaxValueValidator , MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.




class User(AbstractUser):
    phonenumber = models.IntegerField( null=True , blank=True) 
    addres = models.TextField(max_length=100 , null=True , blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'






class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phonenumber = models.IntegerField( null=True , blank=True) 
    addres = models.TextField(max_length=100 , null=True , blank=True)

    def __str__(self):
        return str(self.user)



@receiver(post_save , sender=User)
def creat_user_profile (sender , instance , created , **kwargs):
    if created :
        Profile.objects.create(user=instance)