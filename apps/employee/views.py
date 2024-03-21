from rest_framework import viewsets
from .models import EmployeeDocument, FamilyMember
from .serializers import EmployeeDocumentSerializer, FamilyMemberSerializer


class EmployeeDocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeDocumentSerializer

    def get_queryset(self):
        # Filtrar los documentos por is_active=True
        queryset = EmployeeDocument.objects.filter(is_active=True)
        return queryset


class FamilyMembersViewSet(viewsets.ModelViewSet):
    serializer_class = FamilyMemberSerializer

    def get_queryset(self):
        # Filtrar los documentos por is_active=True
        queryset = FamilyMember.objects.filter(is_active=True)
        return queryset