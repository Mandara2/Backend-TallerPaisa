from django.db import models

class Supplier(models.Model):

    name = models.CharField(max_length=80, null=False, blank=False)

    address = models.CharField(max_length=60, null=False, blank=False)

    phone = models.CharField(max_length=60, null=False, blank=False)

    email = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name