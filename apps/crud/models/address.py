from django.db import models
from apps.crud.models.customer import Customer
from apps.crud.models.city import City

class Address(models.Model):

    locality = models.CharField(max_length=70, null=False, blank=False)

    address_type = models.CharField(max_length=70,null=False, blank=False)

    street = models.CharField(max_length=70,null=False, blank=False)

    address_numer = models.CharField(max_length=70,null=False, blank=False)

    references = models.TextField()

    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                   null=False, blank=False)
    
    city_id = models.ForeignKey(City, on_delete=models.CASCADE,
                                   null=False, blank=False)
    
    def __str__(self):
        return self.locality
