from rest_framework import viewsets

from apps.crud.serializers.installmentSerializer import InstallmentSerializer
from apps.crud.models.installment import Installment

class InstallmentView(viewsets.ModelViewSet):
    serializer_class = InstallmentSerializer
    queryset = Installment.objects.all()