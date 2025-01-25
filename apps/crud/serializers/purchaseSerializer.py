from rest_framework import serializers
from apps.crud.models.purchase import Purchase

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'