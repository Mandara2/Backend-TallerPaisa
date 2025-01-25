from rest_framework import serializers
from apps.crud.models.invoice import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'