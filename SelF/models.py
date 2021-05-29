from django.db import models
import datetime
from django.utils import timezone
import os

class Profile (models.Model):
    PROFILE_CATEGORY = (
        ('Student','Student'),
        ('Professional','Professional'),
    )
    
    UserName = models.CharField(max_length = 50)
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Bio = models.TextField(blank = True)
    University = models.CharField(max_length = 50)
    Profession = models.CharField(max_length=32, default='Student', choices=PROFILE_CATEGORY)
    DOB = models.DateField()
    UserEmail = models.EmailField(max_length = 254)
    Password = models.CharField(max_length = 32)
    

    def __str__ (self):
        return self.UserName