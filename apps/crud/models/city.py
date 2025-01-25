from django.db import models
from apps.crud.models.department import Department

class City(models.Model):
    
    name = models.CharField(max_length=70, null=False, blank=False)

    postal_code = models.CharField(max_length=15, null=False, blank=False)

    department_id = models.ForeignKey(Department, 
                                   on_delete=models.CASCADE,
                                   null=False, blank=False)
    
    def __str__(self):
        return self.name