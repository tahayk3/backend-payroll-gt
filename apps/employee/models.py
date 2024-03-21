from django.db import models

# Create your models here.
class employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    picture = models.CharField(max_length=200)
    dpi = models.CharField(max_length=20)
    data_hiring = models.DateTimeField()
    data_completion = models.DateTimeField()
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    base_salary = models.IntegerField()
    base_salary_initial = models.IntegerField()
    head_department = models.BooleanField()
    method_payment = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    department = models.IntegerField() #ForeignKey
    job_position = models.IntegerField() #ForeignKey
    user = models.IntegerField() #ForeignKey
    company = models.IntegerField() #ForeignKey
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class BaseModel(models.Model):
    """ Abstract Class, BaseModel """
  

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on  was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on  was last modified'
    )

    class Meta:
        """Meta options."""
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']




class EmployeeDocument(BaseModel):
    """ Employee Documents model"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    file = models.CharField(max_length=200) #this field stores a url
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)  # ForeignKey
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
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)# ForeignKey
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self._first_name}{self.last_name}"
