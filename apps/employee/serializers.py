from rest_framework import serializers
from .models import EmployeeDocument, FamilyMember, Employee, SalaryIncrease, Department, JobPositionModel,RequestAbsenceModel


class EmployeeDocumentSerializer(serializers.ModelSerializer):
    """ Employee Document Serializer """
    class Meta:
        model = EmployeeDocument
        fields = [
            'id',
            'name',
            'file',
            'employee',
            'is_active',
            'created',
            'modified'
        ]
        read_only_fields = ['id', 'created', 'modified']


    def create(self, validated_data):
        """ Create Employee Document """
        return EmployeeDocument.objects.create(**validated_data)


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = [
            'id',
            'employee',
            'first_name',
            'last_name',
            'relationship',
            'gender',
            'phone',
            'is_active'
        ]
        read_only_fields = ['id']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

        read_only_fields = ['id']
        
        
        # Instancia de la clase Employee
        def create(self, validated_data):
            employee_instance = Employee.objects.create(**validated_data)
            return employee_instance
        


class SalaryIncreaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryIncrease
        fields = ['id','employee', 'amount', 'reason']


        def create(self, validated_data):
            return SalaryIncrease.objects.create(**validated_data)
        
        
        def update(self, instance, validated_data):
            instance.amount = validated_data.get('amount', instance.amount)
            instance.reason = validated_data.get('reason', instance.reason)
            instance.is_active = validated_data.get('is_active', instance.is_active)
            instance.save()
            return instance
        

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name', 'description', 'company']
        
        
        def create(self, validated_data):
            return Department.objects.create(**validated_data)
        
        
        
class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPositionModel        
        fields =[ 'name', 'description', 'company', 'is_active']

        def create(self, validate_data):
            return JobPositionModel.objects.create(**validate_data)

class RequestAbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestAbsenceModel
        fields = '__all__'

        def create(self, validated_data):
            return RequestAbsenceModel.object.create(**validated_data)
        
