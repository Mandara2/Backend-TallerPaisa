from rest_framework import serializers
from apps.crud.models.branch import Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'