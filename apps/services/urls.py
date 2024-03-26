""" Service URLs"""

# Django
from django.urls import path
from apps.services.views import EmployeeCMSAPIView

urlpatterns = [
    path("cms/employees/", EmployeeCMSAPIView.as_view(), name="cms-employees"),
]
