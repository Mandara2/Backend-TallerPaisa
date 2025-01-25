from django.db import models
from apps.crud.models.customer import Customer

class ShoppingCart(models.Model):

    customer_id = models.OneToOneField(Customer, on_delete=models.CASCADE,
                                       null=False, blank=False)

    creation_date = models.DateField(null=False, blank=False)

    total_amount = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.creation_date