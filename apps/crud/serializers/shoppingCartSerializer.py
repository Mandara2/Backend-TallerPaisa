from rest_framework import serializers
from apps.crud.models.shoppingCart import ShoppingCart

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'