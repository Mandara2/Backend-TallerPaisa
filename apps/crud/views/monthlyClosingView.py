from rest_framework import viewsets

from apps.crud.serializers.monthlyClosingSerializer import MonthlyClosingSerializer
from apps.crud.models.monthlyClosing import MonthlyClosing

class MonthlyClosingView(viewsets.ModelViewSet):
    serializer_class = MonthlyClosingSerializer
    queryset = MonthlyClosing.objects.all()