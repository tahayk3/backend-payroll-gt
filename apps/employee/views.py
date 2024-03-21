from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import EmployeeSerializer, SalaryIncreaseSerializer
from .models import Employee, SalaryIncrease


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [permissions.AllowAny] #Cambiar a IsAuthenticated
    serializer_class = EmployeeSerializer
    

class SalaryIncreaseViewSet(viewsets.ModelViewSet):
    queryset = SalaryIncrease.objects.all()
    permission_classes = [permissions.AllowAny] #Cambiar a IsAuthenticated
    serializer_class = SalaryIncreaseSerializer

