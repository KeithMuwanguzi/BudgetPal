from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250,unique=True, primary_key=True)
    password = models.CharField(max_length=250)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=13,unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.name