from django.db import models

class Product(models.Model): 

    name = models.CharField(max_length=100,
                            null=False, blank=False)

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    available_quantity = models.IntegerField()

    def __str__(self):
        return self.name