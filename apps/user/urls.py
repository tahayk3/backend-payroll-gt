from django.urls import path, include
from . import views


urlpatterns = [
    path('users/', views.UserApi.as_view(), name='users_user'),
    path('users/<int:id>/', views.UserApi.as_view(), name='user_detail'),
    path('login/', views.Login.as_view(), name='login'), 
    path('reset-pass/<int:id>/', views.ResetPassword.as_view(), name='reset_pass'), 
    path('verify/', views.VerifyAccount.as_view(), name='verify_account'), 
] 

"""
Este archivo contiene las URL de la API, que mapean las vistas a las rutas correspondientes
para acceder a diferentes recursos y funcionalidades de la aplicación.

Rutas:
    users/ (GET, PUT, DELETE):
        - GET: Obtiene la lista de todos los usuarios.
        - PUT: Actualiza la información de un usuario existente.
        - DELETE: Elimina un usuario existente.
    
    users/<int:id>/ (GET):
        - DELETE: Obtiene un usuario específico basado en su ID y lo elimina.

    login/ (POST):
        - POST: Permite a un usuario iniciar sesión enviando sus credenciales.

    reset-pass/<int:id>/ (PUT):
        - PUT: Permite a un usuario cambiar su contraseña proporcionando su ID y nueva contraseña.

Vistas:
    - UserApi: Vista para manejar las operaciones de los usuarios, como obtener, actualizar y eliminar.
    - Login: Vista para el inicio de sesión de un usuario.
    - ResetPassword: Vista para restablecer la contraseña de un usuario.
"""
