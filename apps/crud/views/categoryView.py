from rest_framework import viewsets

from apps.crud.serializers.categorySerializer import CategorySerializer
from apps.crud.models.category import Category

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()