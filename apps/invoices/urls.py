# apps/invoices/urls.py
from django.urls import path
from .views import (
    InvoiceListCreateView,
    InvoiceRetrieveUpdateView,
    InvoiceItemListCreateView,
    InvoiceItemRetrieveUpdateDestroyView
)

urlpatterns = [
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceRetrieveUpdateView.as_view(), name='invoice-detail-update'),

    path('items/', InvoiceItemListCreateView.as_view(), name='invoice-item-list-create'),
    path('items/<int:pk>/', InvoiceItemRetrieveUpdateDestroyView.as_view(), name='invoice-item-detail'),
]