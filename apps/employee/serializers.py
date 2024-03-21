from rest_framework import serializers
from .models import EmployeeDocument, FamilyMember


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
from .models import Employee, SalaryIncrease

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
        
        def create(self, validated_data):
            return Employee.objects.create(**validated_data)


class SalaryIncreaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee', 
                  'amount', 
                  'reason']
        
        def create(self, validated_data):
            return SalaryIncrease.objects.create(**validated_data)
        
        
