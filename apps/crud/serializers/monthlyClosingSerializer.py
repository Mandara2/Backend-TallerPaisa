from rest_framework import serializers
from apps.crud.models.monthlyClosing import MonthlyClosing

class MonthlyClosingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyClosing
        fields = '__all__'