from rest_framework import viewsets

from apps.crud.serializers.supplierSerializer import SupplierSerializer
from apps.crud.models.supplier import Supplier

class SupplierView(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

    