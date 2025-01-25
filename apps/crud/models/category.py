from django.db import models
from apps.crud.models.product import Product


class Category(models.Model):

    name = models.CharField(max_length=80, null=False, blank=False)

    description = models.TextField()

    products = models.ManyToManyField('Product', through='ProductCategory')

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    
    product_id = models.ForeignKey(Product, 
                                   on_delete=models.CASCADE, 
                                   null=False, blank=False)
    
    category = models.ForeignKey(Category, 
                                 on_delete=models.CASCADE, 
                                null=False, blank=False)

