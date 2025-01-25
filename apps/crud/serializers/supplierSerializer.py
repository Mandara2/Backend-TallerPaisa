from rest_framework import serializers
from apps.crud.models.supplier import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'