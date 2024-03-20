# django
from django.apps import AppConfig


class PayrollConfig(AppConfig):
    """Payroll module app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.payrolls'
    verbose_name = 'Payroll Module'
