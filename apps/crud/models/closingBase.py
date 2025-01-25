from django.db import models
from apps.crud.models.branch import Branch

# Clase abstracta para los campos comunes
class ClosingBase(models.Model):
    total_sales = models.DecimalField(max_digits=13, decimal_places=2, null=False, blank=False)
    total_expenses = models.DecimalField(max_digits=13, decimal_places=2, null=False, blank=False)
    profits = models.DecimalField(max_digits=13, decimal_places=2, null=False, blank=False)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        abstract = True  # Define esta clase como abstracta