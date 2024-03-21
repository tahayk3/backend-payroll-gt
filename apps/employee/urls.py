from django.urls import path, include

""" views """
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employeeDocuments', views.EmployeeDocumentsViewSet, basename = 'empoyeeDocuments')
router.register(r'familyMember', views.FamilyMembersViewSet, basename='familyMember')

urlpatterns = [
    path('', include(router.urls))

]
