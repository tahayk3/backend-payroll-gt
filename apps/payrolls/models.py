from django.db import models

class PayrollPeriod(models.Model):
    """Payroll Period model"""
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    type = models.CharField(max_length=100)
    company = models.IntegerField(default=0, blank=True)  # Foreign key
    is_open = models.BooleanField(default=False)


class PayrollAccountingTransaction(models.Model):
    """Payroll Accounting Transaction model"""
    employee = models.IntegerField()  # ID del empleado
    type_concept = models.CharField(max_length=255)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    reason = models.CharField(max_length=255)
    total = models.IntegerField()
    date = models.DateTimeField()
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)  # Clave foránea a PayrollPeriod

    def __str__(self):
        return f"PayrollAccountingTransaction: {self.id} - Employee ID: {self.employee}"


class TransferBank(models.Model):
    """Transfer Bank model"""
    employee = models.IntegerField()  # ID del empleado
    date = models.DateTimeField()
    bank = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    reason = models.CharField(max_length=255)
    amount = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)  # Clave foránea a PayrollPeriod

    def __str__(self):
        return f"TransferBank: {self.id} - Employee ID: {self.employee}"


class TransferCash(models.Model):
    """Transfer Cash model"""
    employee = models.IntegerField()  # ID del empleado
    date = models.DateTimeField()
    reason = models.CharField(max_length=255)
    amount = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)  # Clave foránea a PayrollPeriod

    def __str__(self):
        return f"TransferCash: {self.id} - Employee ID: {self.employee}"


class PayrollDeduction(models.Model):
    """Payroll Deduction model"""
    employee = models.IntegerField(default=0, blank=True)  # ID del empleado
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
    employee = models.IntegerField(default=0, blank=True)  # ID del empleado
    type_concept = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)  # Clave foránea a PayrollPeriod

    def __str__(self):
        return f"PayrollIncome: {self.id} - Employee ID: {self.employee}"