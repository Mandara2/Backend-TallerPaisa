from django.db import models
from apps.crud.models.closingBase import ClosingBase


class MonthlyClosing(ClosingBase):
    month_closing = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.month_closing