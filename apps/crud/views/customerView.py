from rest_framework import viewsets

from apps.crud.serializers.customerSerializer import CustomerSerializer
from apps.crud.models.customer import Customer

class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()