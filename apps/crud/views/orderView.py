from rest_framework import viewsets

from apps.crud.serializers.orderSerializer import OrderSerializer
from apps.crud.models.order import Order

class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()