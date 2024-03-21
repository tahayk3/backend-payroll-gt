from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import EmployeeSerializer
from .models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [permissions.AllowAny] #Cambiar a IsAuthenticated
    serializer_class = EmployeeSerializer

   