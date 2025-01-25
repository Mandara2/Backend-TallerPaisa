from rest_framework import viewsets

from apps.crud.serializers.productSerializer import ProductSerializer
from apps.crud.models.product import Product

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()