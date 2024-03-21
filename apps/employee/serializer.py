from rest_framework import serializers
from .models import Employee

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
        
        read_only_fields = ['created_at',]
        
        
