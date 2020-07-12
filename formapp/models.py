from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
# Create your models here.

class Question(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username =  models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    Question1 = models.CharField(max_length=300000,blank=True,null=True)
    Question2 = models.CharField(max_length=300000,blank=True,null=True)
    Question3 = models.CharField(max_length=300000,blank=True,null=True)
    Question4 = models.CharField(max_length=300000,blank=True,null=True)

    def __str__(self):
        return f'{self.user} question' 
