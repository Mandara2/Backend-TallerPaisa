from rest_framework import serializers
from apps.crud.models.sale import Sale

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'