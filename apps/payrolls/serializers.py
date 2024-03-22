# rest framework
from rest_framework import serializers

# models
from apps.payrolls.models import TransferCash, TransferBank, PayrollAccountingTransaction, PayrollPeriod, PayrollDeduction, PayrollIncome, Payroll, PayrollConcept


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


class PayrollAccountingTransactionSerializer(serializers.ModelSerializer):
    """Payroll accounting transaction serializer"""

    class Meta:
        """Meta class"""
        model = PayrollAccountingTransaction
        fields = '__all__'


class TransferBankSerializer(serializers.ModelSerializer):
    """Transfer bank serializer"""

    class Meta:
        """Meta class"""
        model = TransferCash
        fields = '__all__'


class TransferCashSerializer(serializers.ModelSerializer):
    """Transfer cash serializer"""

    class Meta:
        """Meta class"""
        model = TransferCash
        fields = '__all__'
