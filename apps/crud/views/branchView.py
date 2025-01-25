from rest_framework import viewsets

from apps.crud.serializers.branchSerializer import BranchSerializer
from apps.crud.models.branch import Branch

class BranchView(viewsets.ModelViewSet):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()