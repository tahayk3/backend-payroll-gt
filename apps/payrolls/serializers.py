# rest framework
from rest_framework import serializers

# models
from apps.payrolls.models import PayrollPeriod, PayrollDeduction, PayrollIncome, Payroll, PayrollConcept


class PayrollPeriodSerializer(serializers.ModelSerializer):
    """Payroll period serializer"""

    class Meta:
        """Meta class"""
        model = PayrollPeriod
        fields = '__all__'


class PayrollDeductionSerializer(serializers.ModelSerializer):
    """Payroll deduction serializer"""

    class Meta:
        """Meta class"""
        model = PayrollDeduction
        fields = '__all__'


class PayrollIncomeSerializer(serializers.ModelSerializer):
    """Payroll income serializer"""

    class Meta:
        """Meta class"""
        model = PayrollIncome
        fields = '__all__'


class PayrollSerializer(serializers.ModelSerializer):
    """Payroll serializer"""

    class Meta:
        """Meta class"""
        model = Payroll
        fields = '__all__'


class PayrollConceptSerializer(serializers.ModelSerializer):
    """Payroll Concept serializer"""

    class Meta:
        """Meta class"""
        model = PayrollConcept
        fields = '__all__'
