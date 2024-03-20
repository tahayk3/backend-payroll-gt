# rest framework
from rest_framework import viewsets

# serializers
from apps.payrolls.serializers import PayrollPeriodSerializer

# models
from apps.payrolls.models import PayrollPeriod


class PayrollPeriodViewSet(viewsets.ModelViewSet):
    """Payroll period view set """
    serializer_class = PayrollPeriodSerializer
    queryset = PayrollPeriod.objects.all()
