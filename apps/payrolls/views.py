# rest framework
from rest_framework import viewsets

# serializers
from apps.payrolls.serializers import (PayrollPeriodSerializer, PayrollDeductionSerializer,
                                       PayrollIncomeSerializer, PayrollSerializer, PayrollConceptSerializer, 
                                       TransferBankSerializer, TransferCashSerializer,
                                       PayrollAccountingTransactionSerializer, )

# models
from apps.payrolls.models import PayrollPeriod, PayrollDeduction, PayrollIncome, Payroll, PayrollConcept, TransferCash, TransferBank, PayrollAccountingTransaction


class PayrollPeriodViewSet(viewsets.ModelViewSet):
    """Payroll period view set """
    serializer_class = PayrollPeriodSerializer
    queryset = PayrollPeriod.objects.all()


class PayrollDeductionViewSet(viewsets.ModelViewSet):
    """Payroll deduction view set """
    serializer_class = PayrollDeductionSerializer
    queryset = PayrollDeduction.objects.all()


class PayrollIncomeViewSet(viewsets.ModelViewSet):
    """Payroll income view set """
    serializer_class = PayrollIncomeSerializer
    queryset = PayrollIncome.objects.all()


class PayrollViewSet(viewsets.ModelViewSet):
    """Payroll view set"""
    serializer_class = PayrollSerializer
    queryset = Payroll.objects.all()


class PayrollConceptViewSet(viewsets.ModelViewSet):
    """Payroll concept view set """
    serializer_class = PayrollConceptSerializer
    queryset = PayrollConcept.objects.all()


class TransferCashViewSet(viewsets.ModelViewSet):
    """Transfer cash view set"""
    serializer_class = TransferCashSerializer
    queryset = TransferCash.objects.all()

class TransferBankViewSet(viewsets.ModelViewSet):
    """Transfer bank view set"""
    serializer_class = TransferBankSerializer
    queryset = TransferBank.objects.all()

class PayrollAccountingTransactionViewSet(viewsets.ModelViewSet):
    """Payroll accounting transaction view set"""
    serializer_class = PayrollAccountingTransactionSerializer
    queryset = PayrollAccountingTransaction.objects.all()
