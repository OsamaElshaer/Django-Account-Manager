from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phonenumber = models.IntegerField( validators=[MaxValueValidator(100),MinValueValidator(1) ] , null=True , blank=True) 
    addres = models.TextField(max_length=100 , null=True , blank=True)