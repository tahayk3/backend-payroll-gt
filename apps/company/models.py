from django.db import models
from django.core.validators import RegexValidator

class Company(models.Model):
    
    name = models.CharField(
        'name company',
        unique = True,
        max_length = 150,
        error_messages = {
            'unique': 'A company with that name already exists'
        }
    )

    phone_regex = RegexValidator(
        regex= r'^\d{8}$',
        message = "Phone number must be entered in the format: +99999999"
    )
    phone = models.CharField( validators= [phone_regex] , max_length = 8)

    description = models.TextField()

    address = models.CharField(max_length = 150)

    picture = models.TextField()

    is_active = models.BooleanField(
        default = True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['name', 'phone', 'description', 'address']

    def __str__(self):
        return self.name
    


