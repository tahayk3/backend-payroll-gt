from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  
        fields = ['id', 'username', 'email', 'role', 'picture', 'password', 'company', 'is_active', 'is_default_password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.is_default_password = False  
        else:
            instance.set_password('12345')
        instance.save()
        return instance