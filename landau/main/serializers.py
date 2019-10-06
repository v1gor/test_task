from .models import Balance, Capital

from rest_framework import serializers


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'


class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = '__all__'
