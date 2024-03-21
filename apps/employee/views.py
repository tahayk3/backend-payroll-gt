from rest_framework.response import Response

from .serializers import EmployeeDocumentSerializer, FamilyMemberSerializer
from django.shortcuts import render
from rest_framework import viewsets, permissions, status

""" MODELS """
from .models import Employee
from .models import EmployeeDocument, FamilyMember
from rest_framework import viewsets, permissions
from .serializers import EmployeeSerializer, SalaryIncreaseSerializer
from .models import Employee, SalaryIncrease

""" SERIALIZERS """
from .serializers import EmployeeSerializer
from .serializers import EmployeeSerializer, SalaryIncreaseSerializer


class EmployeeDocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeDocumentSerializer

    def get_queryset(self):
        # Filtrar los documentos por is_active=True
        queryset = EmployeeDocument.objects.filter(is_active=True)
        return queryset

    def create(self, request, *args, **kwargs):
        # Validar si el empleado existe
        employee_id = request.data.get('employee')
        if not Employee.objects.filter(id=employee_id).exists():
            return Response({'error': 'El empleado especificado no existe'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class FamilyMembersViewSet(viewsets.ModelViewSet):
    serializer_class = FamilyMemberSerializer

    def get_queryset(self):
        # Filtrar los miembros de la familia por is_active=True
        queryset = FamilyMember.objects.filter(is_active=True)
        return queryset

    def create(self, request, *args, **kwargs):
        # Validar si el empleado existe
        employee_id = request.data.get('employee')
        if not Employee.objects.filter(id=employee_id).exists():
            return Response({'error': 'El empleado especificado no existe'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [permissions.AllowAny] #Cambiar a IsAuthenticated
    serializer_class = EmployeeSerializer
    

class SalaryIncreaseViewSet(viewsets.ModelViewSet):
    queryset = SalaryIncrease.objects.all()
    permission_classes = [permissions.AllowAny] #Cambiar a IsAuthenticated
    serializer_class = SalaryIncreaseSerializer

   
