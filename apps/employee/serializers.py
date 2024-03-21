""" django Rest Framework """
from rest_framework import serializers

""" Models """
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

        read_only_fields = ['id']
       

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
            'is_active']
        read_only_fields = ['id']
