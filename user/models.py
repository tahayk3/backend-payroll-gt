from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company']

    role = models.CharField(max_length=50, null=True)
    picture = models.ImageField(upload_to='pictures/', blank= True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    company = models.PositiveBigIntegerField(null=True) #agregar FK.
    is_active = models.BooleanField(default=True)
    is_default_password = models.BooleanField(default=True) 


    def _str_(self):
        return self.email    
  