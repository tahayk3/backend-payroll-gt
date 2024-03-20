# rest framework
from rest_framework import serializers

# models
from apps.payrolls.models import PayrollPeriod


class PayrollPeriodSerializer(serializers.ModelSerializer):
    """Payroll period serializer"""

    class Meta:
        """Meta class"""
        model = PayrollPeriod
        fields = '__all__'
