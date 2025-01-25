from django.db import models

class Department(models.Model):

    name = models.CharField(max_length=40, null=False, blank=False)

    region = models.CharField(max_length=40)

    def __str__(self):
        return self.name