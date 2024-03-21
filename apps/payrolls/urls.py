# django
from django.urls import path, include

# rest framework
from rest_framework.routers import DefaultRouter

# view sets
from apps.payrolls.views import PayrollPeriodViewSet, PayrollDeductionViewSet, PayrollIncomeViewSet

router = DefaultRouter()

router.register(
     r'payroll-periods',
     PayrollPeriodViewSet,
     basename='payroll-periods',
)

router.register(
    r'payroll-deductions',
    PayrollDeductionViewSet,
    basename='payroll-deductions',
)

router.register(
    r'payroll-incomes',
    PayrollIncomeViewSet,
    basename='payroll-incomes',
)

urlpatterns = [
    path('api/v1/', include(router.urls))
]