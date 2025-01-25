from django.db import models
from apps.crud.models.address import Address


class Branch(models.Model):

    name = models.CharField(max_length=70, null=False, blank=False)

    storage_capacity = models.IntegerField(null=False, blank=False)
    
    phone = models.CharField(max_length=60, null=False, blank=False)

    address_id =  models.OneToOneField(Address, on_delete=models.CASCADE,
                                   null=False, blank=False)
    
    def __str__(self):
        return self.name
    