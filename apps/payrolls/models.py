from django.db import models

from apps.employee.models import Employee
from apps.company.models import Company


class PayrollPeriod(models.Model):
    """Payroll Period model"""
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    type = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Foreign key
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PayrollAccountingTransaction(models.Model):
    """Payroll Accounting Transaction model"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Usamos ForeignKey para relacionar con Employee
    type_concept = models.CharField(max_length=255)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    reason = models.CharField(max_length=255)
    total = models.IntegerField()
    date = models.DateTimeField()
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)

    def __str__(self):
        return f"PayrollAccountingTransaction: {self.id} - Employee: {self.employee}"


class TransferBank(models.Model):
    """Transfer Bank model"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Usamos ForeignKey para relacionar con Employee
    date = models.DateTimeField()
    bank = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    reason = models.CharField(max_length=255)
    amount = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)

    def __str__(self):
        return f"TransferBank: {self.id} - Employee: {self.employee}"


class TransferCash(models.Model):
    """Transfer Cash model"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Usamos ForeignKey para relacionar con Employee
    date = models.DateTimeField()
    reason = models.CharField(max_length=255)
    amount = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)

    def __str__(self):
        return f"TransferCash: {self.id} - Employee: {self.employee}"


class PayrollDeduction(models.Model):
    """Payroll Deduction model"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type_concept = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)  # Clave foránea a PayrollPeriod

    def __str__(self):
        return f"PayrollDeduction: {self.id} - Employee ID: {self.employee}"
    
    
class PayrollIncome(models.Model):
    """Payroll Income model"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type_concept = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)  # Clave foránea a PayrollPeriod

    def __str__(self):
        return f"PayrollIncome: {self.id} - Employee ID: {self.employee}"


class Payroll(models.Model):
    """Payroll model"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE) # company
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)

    date_generated = models.DateTimeField()
    total = models.IntegerField()
    is_open = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PayrollConcept(models.Model):
    """Payroll Concept model"""
    concept = models.CharField(max_length=100)

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) # foreign key
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE) # foreign key

    date = models.DateTimeField()
    reason = models.CharField(max_length=100)
    overtime_minutes = models.IntegerField(default=0)
    public_holiday = models.BooleanField(default=False)
    sales = models.IntegerField()
    production = models.IntegerField()
    amount = models.IntegerField()
    is_cancelled = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
