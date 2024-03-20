# django
from django.urls import path, include

# rest framework
from rest_framework.routers import DefaultRouter

# view sets
from apps.payrolls.views import PayrollPeriodViewSet

router = DefaultRouter()

router.register(
    r'payroll-periods',
    PayrollPeriodViewSet,
    basename='payroll-periods',
)

urlpatterns = [
    path('api/v1/', include(router.urls))
]