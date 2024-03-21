# django
from django.urls import path, include

# rest framework
from rest_framework.routers import DefaultRouter

# view sets
from apps.payrolls.views import (PayrollPeriodViewSet, PayrollDeductionViewSet,
                                 PayrollIncomeViewSet, PayrollViewSet, PayrollConceptViewSet)

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

router.register(
    r'payrolls',
    PayrollViewSet,
    basename='payrolls'
)

router.register(
    r'payroll-concepts',
    PayrollConceptViewSet,
    basename='payroll-concepts'
)

urlpatterns = [
    path('api/v1/', include(router.urls))
]