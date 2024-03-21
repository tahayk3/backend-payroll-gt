from django.urls import path, include
from rest_framework import routers
from apps.employee.views import EmployeeViewSet, SalaryIncreaseViewSet, DepartmentViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'salary-increase', SalaryIncreaseViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
