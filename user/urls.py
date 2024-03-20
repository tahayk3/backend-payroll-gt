from django.urls import path, include
from . import views


urlpatterns = [
    path('users/', views.UserApi.as_view(), name='users_user'),
    path('users/admin/', views.UserApiAdmin.as_view(), name='users_admin'),
    path('users/<int:id>/', views.UserApi.as_view(), name='user_detail'),
    path('login/', views.Login.as_view(), name='login'),
] 