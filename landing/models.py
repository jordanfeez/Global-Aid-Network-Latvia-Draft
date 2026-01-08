from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model
# Create your models here.'
#
User = get_user_model() 

#class User(auth.models.User,auth.models.PermissionsMixin):

    #def __str__(self):
       # return "@{}".format(self.username)

class GenderChoice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='gender')
    Gender_Choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    gender = models.CharField(max_length=10, choices=Gender_Choices)

class Address(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='address',)
    #Address line 1
    address_one = models.CharField(max_length=100)
    #Address line 2
    address_two = models.CharField(max_length=100)
    #City 
    city = models.CharField(max_length=100)                 
    #Zipcode
    zipcode=models.CharField(max_length=10)
    #Country
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address_one}, {self.city}, {self.zipcode},{self.country}"
