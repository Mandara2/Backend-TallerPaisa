from rest_framework import viewsets

from apps.crud.serializers.departmentSerializer import DepartmentSerializer
from apps.crud.models.department import Department

class DepartmentView(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()