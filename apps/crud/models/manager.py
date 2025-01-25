from django.db import models
from apps.crud.models.branch import Branch

class Manager(models.Model):

    first_name = models.CharField(max_length=60, null=False, blank=False)

    second_name = models.CharField(max_length=60)

    surname = models.CharField(max_length=100, null=False, blank=False)

    email = models.CharField(max_length=60, null=False, blank=False)

    phone = models.CharField(max_length=40, null=False, blank=False)

    hiring_date = models.DateField()

    salary = models.DecimalField(max_digits=13, decimal_places=2)

    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE,
                                   null=False, blank=False)
    
    def __str__(self):
        return self.first_name