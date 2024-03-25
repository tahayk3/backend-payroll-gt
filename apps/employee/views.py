from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from django.shortcuts import render
from django.db import transaction


""" SERIALIZERS """
from .serializers import  EmployeeSerializer, SalaryIncreaseSerializer, DepartmentSerializer, EmployeeDocumentSerializer, FamilyMemberSerializer, JobPositionSerializer, RequestAbsenceSerializer
from apps.user.serializers import UserSerializer

""" MODELS """
from .models import EmployeeDocument, FamilyMember, Employee, SalaryIncrease, Department, JobPositionModel, RequestAbsenceModel
from apps.company.models import Company
from apps.user.models import User


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
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        # Filtrar empleados de una empresa específica
        company_id = self.request.query_params.get('company')
        if company_id:
            queryset = Employee.objects.filter(company=company_id)
        else:
            queryset = Employee.objects.all()
        return queryset
    
    
    
    """ Crear un empleado con un usuario, tomando en cuenta que para ello se llama al metodo create_user de User
        y se envia el id del usuario creado al modelo Employee
    """
    def create(self, request, *args, **kwargs):

        user_data = {
            'email': request.data.get('email'),
            'username': request.data.get('username')
        }

        user_serializer = UserSerializer(data=user_data)
        if not user_serializer.is_valid():
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        with transaction.atomic():
            user_instance = User()
            user_instance.create_user(**user_data)
            request.data['user'] = user_instance.id

            # Crear el empleado
            employee_serializer = EmployeeSerializer(data=request.data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return Response(employee_serializer.data, status=status.HTTP_201_CREATED)
            else:
                transaction.set_rollback(True)
                return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalaryIncreaseViewSet(viewsets.ModelViewSet):
    queryset = SalaryIncrease.objects.all()
    permission_classes = [permissions.AllowAny] #Cambiar a IsAuthenticated
    serializer_class = SalaryIncreaseSerializer

    #Llamar el metodo save de SalaryIncrease
    def create(self, request, *args, **kwargs):
        employee_id = request.data.get('employee')
        amount = request.data.get('amount')
        reason = request.data.get('reason')
        if not Employee.objects.filter(id=employee_id).exists():
            return Response({'error': 'El empleado especificado no existe'}, status=status.HTTP_400_BAD_REQUEST)
        if not amount or not reason:
            return Response({'error': 'Debe especificar el monto y la razón del aumento de salario'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    
    # Filtrar aumentos de salario por empleado
    def get_queryset(self):
        employee_id = self.request.query_params.get('employee')
        if employee_id:
            queryset = SalaryIncrease.objects.filter(employee=employee_id)
        else:
            queryset = SalaryIncrease.objects.all()
        return queryset
    
    # Llamar el metodo delete de SalaryIncrease
    def delete(self, request, *args, **kwargs):
        salary_increase_id = kwargs.get('pk')
        salary_increase = SalaryIncrease.objects.get(id=salary_increase_id)
        salary_increase.delete()
        return Response({'message': 'Aumento de salario eliminado correctamente'}, status=status.HTTP_200_OK)
    


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [permissions.AllowAny] #Cambiar a IsAuthenticated
    serializer_class = DepartmentSerializer

    # Filtrar departamentos por empresa
    def get_queryset(self):
        company_id = self.request.query_params.get('company')
        if company_id:
            queryset = Department.objects.filter(company=company_id)
        else:
            queryset = Department.objects.all()
        return queryset


    def create(self, request, *args, **kwargs):
        
        company_id = request.data.get('company')
        if not Company.objects.filter(id=company_id).exists():
            return Response({'error': 'La empresa especificada no existe'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class JobPositionViewSet(viewsets.ModelViewSet):
    serializer_class = JobPositionSerializer
    permission_classes = [permissions.AllowAny] #Cambiar a IsAuthenticated


    def get_queryset(self):
        # Filtrar los jobPosition by is_active
        queryset = JobPositionModel.objects.filter(is_active=True)
        return queryset
    

    def create(self, request, *args, **kwargs):
         return super().create(request, *args, **kwargs)


class RequestAbsenceViewSet(viewsets.ModelViewSet):
    serializer_class = RequestAbsenceSerializer
    permission_classes = [permissions.AllowAny] #Cambiar a IsAuthenticated

    def get_queryset(self):
        # Filtrar los requestAbsence by is_active
        queryset = RequestAbsenceModel.objects.filter(is_active=True)
        return queryset

    def create(self, request, *args, **kwargs):
        # Validar si el empleado existe
        employee_id = request.data.get('employee')
        if not Employee.objects.filter(id=employee_id).exists():
            return Response({'error': 'El empleado especificado no existe'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
