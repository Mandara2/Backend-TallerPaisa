from django.db import models
from apps.crud.models.closingBase import ClosingBase

class DailyClosing(ClosingBase):
    closing_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.closing_date