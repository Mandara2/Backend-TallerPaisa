from django.db import models
from apps.crud.models.employee import Employee

class Sale(models.Model):

    sale_date = models.DateField(null=False, blank=False)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False)

    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                   null=False, blank=False)
    
    def __str__(self):
        return self.sale_date