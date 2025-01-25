from django.db import models
from apps.crud.models.purchase import Purchase

class Installment(models.Model):

    number = models.IntegerField(null=False, blank=False)

    amount = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False)

    interest = models.DecimalField(max_digits=8, decimal_places=4)

    purchase_id = models.ForeignKey(Purchase, on_delete=models.CASCADE, 
                                null=False, blank=False)
    
    def __str__(self):
        return self.number