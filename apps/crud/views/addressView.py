from rest_framework import viewsets
from apps.crud.serializers.addressSerializer import AddressSerializer
from apps.crud.models.address import Address

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()