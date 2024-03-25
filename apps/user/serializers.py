from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User.

    Este serializador se utiliza para convertir los objetos User en representaciones JSON
    y viceversa.
    """
    class Meta:
        model = User  
        fields = ['id', 'username', 'email', 'role', 'picture', 'password', 'company', 'is_active', 'is_default_password']

    def create(self, validated_data):
        """
        Este método crea un nuevo usuario con los datos validados proporcionados.
        La contraseña se convierte en hash utilizando la función 'make_password'.
        Si no se proporciona una contraseña, se utiliza una contraseña predeterminada.

        Returns:
            instance (User): La instancia del usuario creado.
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.password = make_password(password)
            instance.is_default_password = False
        else:
            instance.password = make_password('12345')
        instance.save()
        return instance
    

class CustomUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['email', 'username', 'picture']