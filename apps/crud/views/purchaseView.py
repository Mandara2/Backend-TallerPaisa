from rest_framework import viewsets

from apps.crud.serializers.purchaseSerializer import PurchaseSerializer
from apps.crud.models.purchase import Purchase

class PurchaseView(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()