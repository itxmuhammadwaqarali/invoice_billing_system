
from apps.invoices.models import Invoice

from django.db import models
class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    method = models.CharField(max_length=50)  # e.g., Credit Card, Bank Transfer
    status = models.CharField(max_length=20, default='completed')  # completed, failed

