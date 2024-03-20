# django
from django.db import models


class PayrollPeriod(models.Model):
    """Payroll Period model"""
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    type = models.CharField(max_length=100)

    company = models.IntegerField(default=0, blank=True) # foreign key

    is_open = models.BooleanField(default=False)
