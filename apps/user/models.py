from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.company.models import Company
from django.contrib.auth.hashers import make_password


class User(AbstractUser):
    """
    Modelo personalizado de usuario.

    Este modelo extiende el modelo base de usuario de Django y agrega campos adicionales
    como email, role, picture, company, entre otros.

    """
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    role = models.CharField(max_length=50, null=True)
    picture = models.TextField(blank= True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='user', null=True)
    is_active = models.BooleanField(default=True)
    is_default_password = models.BooleanField(default=True) 


    def create_user_admin(self, email, password, instance_company):
        """
        Este método crea un nuevo usuario con el rol de 'admin' y asigna los valores
        proporcionados para el email, contraseña, nombre de usuario y compañía.

        Returns:
            User: El nuevo usuario creado con rol de 'admin'.
        """
        self.company = instance_company
        self.email = email
        self.username = instance_company.name
        self.picture = instance_company.picture
        self.role = 'admin'
        self.is_default_password = False
        self.password = make_password(password)
        self.save()
        return self
    
    def create_user(self, email, username):
        """
        Este método crea un nuevo usuario con el rol de 'user' y asigna los valores
        proporcionados para el email y el nombre de usuario. La contraseña se establece
        como la predeterminada '12345'.

        Returns:
            User: El nuevo usuario creado con rol de 'user' y contraseña predeterminada.
        """
        self.email = email
        self.username = username
        self.role = 'user'
        self.password = make_password('12345')
        self.save()
        return self


    def __str__(self):  
        """
        Retorna la representación en cadena del usuario.
        En este caso, la representación es el email del usuario.

        Returns:
            str: El email del usuario.
        """
        return self.email    


