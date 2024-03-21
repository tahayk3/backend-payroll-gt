from rest_framework import serializers
from .models import Employee, SalaryIncrease, Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
        
        def create(self, validated_data):
            return Employee.objects.create(**validated_data)


class SalaryIncreaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryIncrease
        fields = ['employee', 'amount', 'reason']


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
        fields = ['name', 'description', 'company']
        
        
        def create(self, validated_data):
            return Department.objects.create(**validated_data)
        
        
        
        