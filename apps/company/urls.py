# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from apps.company.views import CompanyViewSet

router = DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls))
]
