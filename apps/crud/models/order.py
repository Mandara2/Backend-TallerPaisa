from django.db import models
from apps.crud.models.product import Product
from apps.crud.models.manager import Manager
from apps.crud.models.supplier import Supplier

class Order(models.Model): 

    order_date = models.DateField(null=False, blank=False)

    status = models.BooleanField()

    total_amount = models.DecimalField(max_digits=13, decimal_places=2, null=False, blank=False)

    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE,
                                   null=False, blank=False)
    
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE,
                                   null=False, blank=False)

    products = models.ManyToManyField('Product', through='OrderProduct')

    def __str__(self):
        return self.order_date


class OrderProduct(models.Model):

    order_id = models.ForeignKey(Order,
                                on_delete=models.CASCADE, 
                                null=False, blank=False)
    
    product_id = models.ForeignKey(Product,
                                on_delete=models.CASCADE, 
                                null=False, blank=False)
    
    quantity = models.IntegerField()