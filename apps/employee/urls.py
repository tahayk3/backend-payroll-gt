from django.urls import path, include

""" views """
from . import views
from apps.employee import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'employeeDocuments', views.EmployeeDocumentsViewSet, basename = 'empoyeeDocuments')
router.register(r'familyMember', views.FamilyMembersViewSet, basename='familyMember')
router.register(r'employees', views.EmployeeViewSet)
router.register(r'salary-increase', views.SalaryIncreaseViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'jobPosition', views.JobPositionViewSet, basename='jobposition')
router.register(r'requestAbsence', views.RequestAbsenceViewSet, basename='requestabsence')

urlpatterns = [
    path('', include(router.urls)),
]


