from rest_framework import viewsets

from apps.crud.serializers.dailyClosingSerializer import DailyClosingSerializer
from apps.crud.models.dailyClosing import DailyClosing

class DailyClosingView(viewsets.ModelViewSet):
    serializer_class = DailyClosingSerializer
    queryset = DailyClosing.objects.all()