from django.db import models
from apps.clients.models import Client
from apps.accounts.models import User
from apps.invoices.helping import STATUS_CHOICES


class InvoiceItem(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        qty = self.quantity or 0
        price = self.unit_price or 0
        self.total_price = qty * price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} ({self.quantity})"


class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    invoice_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    items=models.ManyToManyField(InvoiceItem)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            count = Invoice.objects.count() + 1
            self.invoice_number = f'INV{count:03d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number or f"Invoice {self.pk}"

