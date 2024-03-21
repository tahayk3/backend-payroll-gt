# rest framework
from rest_framework import viewsets

# serializers
from apps.payrolls.serializers import PayrollPeriodSerializer, PayrollDeductionSerializer, PayrollIncomeSerializer

# models
from apps.payrolls.models import PayrollPeriod, PayrollDeduction, PayrollIncome


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