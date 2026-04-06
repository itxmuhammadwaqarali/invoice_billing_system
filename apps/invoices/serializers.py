# apps/invoices/serializers.py
from rest_framework import serializers
from .models import Invoice, InvoiceItem
from apps.accounts.models import User
from apps.clients.models import Client

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['id', 'invoice', 'description', 'quantity', 'unit_price', 'total_price']
        read_only_fields = ['id']

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True, read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Invoice
        fields = ['id', 'client', 'created_by', 'invoice_number', 'date', 'due_date', 'status', 'total_amount', 'tax', 'items']
        read_only_fields = ['id', 'invoice_number', 'date', 'created_by']

