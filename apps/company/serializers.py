from rest_framework import serializers

from apps.company.models import Company

from rest_framework.validators import UniqueValidator

class CompanyModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields= (
            'id', 'name', 'phone', 'description', 'address',
            'picture', 'is_active', 'created_at'
        )

    def create(self, validated_data):
        # Crear la compañía como se hace normalmente
        company_instance = Company.objects.create(**validated_data)
        return company_instance

