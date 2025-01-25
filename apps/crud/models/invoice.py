from django.db import models
from apps.crud.models.installment import Installment

class Invoice(models.Model):

    issue_date = models.DateField(null=False, blank=False)

    total_amount = models.DecimalField(max_digits=13, decimal_places=2, null=False, blank=False)

    installment_id = models.ForeignKey(Installment, on_delete=models.CASCADE,
                                   null=False, blank=False)
    
    def __str__(self):
        return self.issue_date