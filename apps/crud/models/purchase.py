from django.db import models
from apps.crud.models.customer import Customer

class Purchase(models.Model):
    
    date = models.DateField()

    amount = models.DecimalField(max_digits=13, decimal_places=2)

    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                   null=False, blank=False)
    
    def __str__(self):
        return self.date

    