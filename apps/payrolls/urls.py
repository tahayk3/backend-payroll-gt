from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.payrolls.views import (PayrollPeriodViewSet, PayrollDeductionViewSet,
                                 PayrollIncomeViewSet, PayrollViewSet, PayrollConceptViewSet,
                                 TransferCashViewSet, TransferBankViewSet, 
                                 PayrollAccountingTransactionViewSet)

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

router.register(
    r'transfer-cash',
    TransferCashViewSet,
    basename='transfer-cash'
)

router.register(
    r'transfer-bank',
    TransferBankViewSet,
    basename='transfer-bank'
)

router.register(
    r'payroll-accounting-transactions',
    PayrollAccountingTransactionViewSet,
    basename='payroll-accounting-transactions'
)

urlpatterns = [
    path('api/v1/', include(router.urls))
]
