from rest_framework import viewsets

from apps.crud.serializers.shoppingCartSerializer import ShoppingCartSerializer
from apps.crud.models.shoppingCart import ShoppingCart

class ShoppingCartView(viewsets.ModelViewSet):
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects.all()