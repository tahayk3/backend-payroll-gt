from django.urls import path, include
from rest_framework import routers
from apps.employee import views

router = routers.DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
