from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from apps.company.serializers import CompanyModelSerializer
from apps.company.models import Company

def tu_metodo_de_companero(user_data):
    print("Datos recibidos para crear el usuario:")
    print(user_data)

    return "success"

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer

    def create(self, request, *args, **kwargs):

        # Procesar los datos de la solicitud para crear la compañía
        serializer = CompanyModelSerializer(data=request.data)
        if serializer.is_valid():
            company_instance = serializer.save()
            print("Datos de la compañía creada:")
            print(serializer.data)

            user_data = {
                'username': request.data['username'],  # Usar request.data['username'] en lugar de request.data.get('username')
                'email': request.data.get('email'),
                'password': request.data.get('password'),
                'company_id': company_instance.id
            }

      
            create_user_result = tu_metodo_de_companero(user_data)

       
            if create_user_result == "success":
                return Response({"message": "Company and user created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to create user"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
