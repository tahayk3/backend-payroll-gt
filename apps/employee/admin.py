from django.contrib import admin
from .models import Employee, JobPositionModel, RequestAbsenceModel, Department

# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)

admin.site.register(JobPositionModel)
admin.site.register(RequestAbsenceModel)