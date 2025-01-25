from rest_framework import viewsets

from apps.crud.serializers.managerSerializer import ManagerSerializer
from apps.crud.models.manager import Manager

class ManagerView(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()