from rest_framework import viewsets

from apps.crud.serializers.invoiceSerializer import InvoiceSerializer
from apps.crud.models.invoice import Invoice

class InvoiceView(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()