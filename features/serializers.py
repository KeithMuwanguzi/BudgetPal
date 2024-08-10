from rest_framework import serializers
from income_expenses.models import IncomeData, ExpenseData

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeData
        fields = ['id', 'amount', 'date', 'category', 'description']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseData
        fields = ['id', 'amount', 'date', 'category', 'description']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
