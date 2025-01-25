from rest_framework import serializers
from apps.crud.models.dailyClosing import DailyClosing

class DailyClosingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyClosing
        fields = '__all__'