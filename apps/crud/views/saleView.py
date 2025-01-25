from rest_framework import viewsets

from apps.crud.serializers.saleSerializer import SaleSerializer
from apps.crud.models.sale import Sale

class SaleView(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()