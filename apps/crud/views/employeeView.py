from rest_framework import viewsets

from apps.crud.serializers.employeeSerializer import EmployeeSerializer
from apps.crud.models.employee import Employee

class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()