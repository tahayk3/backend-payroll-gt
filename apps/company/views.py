from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from apps.company.serializers import CompanyModelSerializer
from apps.company.models import Company
from .permissions.company import IsCompanySuperAdmin



from apps.user.models import User


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer
    permission_classes = [IsCompanySuperAdmin]

    def create(self, request, *args, **kwargs):
        
        serializer = CompanyModelSerializer(data=request.data)
        if serializer.is_valid():
            # Creacion de compañía
            company_instance = serializer.save()
            print("Datos de la compañía creada:")
            print(serializer.data)

            #diccionario de datos a pasar
            user_data = {
                'email': request.data.get('email'),
                'password': request.data.get('password'),
                'instance_company': company_instance 
            }

            # Creacion de instancia y pasada de datos a User
            user_instance = User()

            create_user_result = user_instance.create_user_admin(**user_data)

            if create_user_result:
                return Response({"message": "Company and user created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to create user"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        instance.is_active = False
        instance.save()

        return Response({"message": "Company deactivated successfully"}, status=status.HTTP_204_NO_CONTENT)

    
    def get_queryset(self):
        return Company.objects.filter(is_active=True)