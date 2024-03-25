from .models import User
from .serializers import UserSerializer
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from apps.company.models import Company


class UserApi(APIView):
    """
    Vista para gestionar usuarios.
    Esta vista permite realizar operaciones CRUD (Leer, Actualizar, Eliminar) en los usuarios.

    Args:
        APIView: Clase base para todas las vistas de la API de Django Rest Framework.
    """

    def get(self, request):
        """
        Esta función obtiene todos los usuarios de la base de datos y los serializa
        para devolverlos en formato JSON como respuesta.

        Returns:
            Response: Un objeto de respuesta con la lista de usuarios y un estado HTTP 200 OK.
        """
        
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):
        """
        Esta función actualiza los detalles de un usuario existente utilizando su ID.
        Toma los datos proporcionados en la solicitud y los actualiza en la base de datos.

        Returns:
            Response: Un objeto de respuesta con los detalles del usuario actualizado y un estado HTTP 204.
        """
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        """
        Esta función cambia el estado de un usuario a 'inactivo', lo que es equivalente a eliminarlo
        de forma lógica. El usuario no se elimina físicamente de la base de datos.

        Returns:
            Response: Un objeto de respuesta con un mensaje de éxito y un estado HTTP 204 NO CONTENT.
        """
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user_delete = {'is_active': False}
        serializer = UserSerializer(user, data=user_delete, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    """
    Vista para el inicio de sesión de un usuario.

    Esta vista maneja el proceso de autenticación de un usuario
    utilizando el email y la contraseña proporcionados.

    Args:
        APIView: Clase base para todas las vistas de la API de Django Rest Framework.
    """
    def post(self, request):
        """
        Procesa la solicitud POST para el inicio de sesión de un usuario.

        Esta función toma el email y la contraseña proporcionados en la solicitud
        POST, y luego utiliza la función 'authenticate' de Django para verificar
        si las credenciales son válidas.

        Returns:
            Response: Un objeto de respuesta con un mensaje de estado según el resultado de la autenticación.
        """
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            serializer = CustomUserSerializer(user)
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
        

class ResetPassword(APIView):
    """
    Vista para restablecer la contraseña de un usuario.

    Args:
        APIView: Clase base para todas las vistas de la API de Django Rest Framework.
    """
    def put(self, request, id):
        """
        Esta función toma el ID del usuario y los datos de la nueva contraseña
        proporcionados en la solicitud PUT, y luego actualiza la contraseña
        del usuario en la base de datos.

        Returns:
            Response: Un objeto de respuesta con un mensaje de éxito si la contraseña se cambió con éxito.
        """
        user = get_object_or_404(User, id=id)

        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        
        if password != confirm_password:
            return Response({"message": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
        
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        user.password = make_password(password)
        user.save()
        
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    

class VerifyAccount(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).exists()
        if user:
            return Response({'exist': True}, status=status.HTTP_200_OK)
        else:
            return Response({'exist': False}, status=status.HTTP_400_BAD_REQUEST)



        



