from rest_framework import viewsets

from apps.crud.serializers.citySerializer import CitySerializer
from apps.crud.models.city import City

class CityView(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()