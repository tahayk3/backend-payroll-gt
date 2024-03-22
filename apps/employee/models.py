from django.db import models
from core.utils.models import BaseModel
from apps.company.models import Company
from apps.user.models import User

# Employee 

class Department(models.Model):

    """Department Model"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE) #ForeignKey
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.name}"
    

class Employee(models.Model):

    """Employee Model"""
    
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    picture = models.CharField(max_length=200)
    dpi = models.CharField(max_length=20)
    date_hiring = models.DateField(blank=True, null=True)
    date_completion = models.DateField(blank=True, null=True)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    base_salary = models.IntegerField()
    base_salary_initial = models.IntegerField()
    head_department = models.BooleanField(default=False)
    method_payment = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE) #ForeignKey
    job_position = models.IntegerField() #ForeignKey
    user = models.ForeignKey(User, on_delete=models.CASCADE) #ForeignKey
    company = models.ForeignKey(Company, on_delete=models.CASCADE)#ForeignKey
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class EmployeeDocument(BaseModel):
    """ Employee Documents model"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    file = models.CharField(max_length=200) #this field stores a url
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # ForeignKey
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name}"



class FamilyMember(BaseModel):
    """ Family Member model"""

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    gender = models.CharField(max_length = 100)
    phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)# ForeignKey
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self._first_name}{self.last_name}"
    
    
class SalaryIncrease(models.Model):

    """Salary Increase Model"""
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) #ForeignKey
    amount = models.IntegerField()
    reason = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.reason}"
    
class JobPositionModel(models.Model):
    name = models.CharField( max_length=150)
    description = models.CharField(max_length=200)
    company = models.IntegerField()
    is_active = models.BooleanField()
    
    def __str__(self):
        return f"{self.name}"
    
class RequestAbsenceModel(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) 
    company = models.IntegerField() #FK 
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField( max_length=200)
    status = models.CharField(max_length=100)
    is_active = models.BooleanField()
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return f"{self.reason}"
    
    