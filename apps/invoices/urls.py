# apps/invoices/urls.py
from django.urls import path
from .views import (
    # API Views
    InvoiceListCreateView,
    InvoiceRetrieveUpdateView,
    InvoiceItemListCreateView,
    InvoiceItemRetrieveUpdateDestroyView,
    # Web Views
    DashboardView,
    InvoiceListWebView,
    InvoiceDetailWebView,
    InvoiceCreateWebView,
    InvoiceUpdateWebView,
    InvoiceDeleteWebView,
    InvoicePrintView,
)

urlpatterns = [
    # ============================================================================
    # WEB ROUTES (Frontend Pages)
    # ============================================================================
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('invoices/', InvoiceListWebView.as_view(), name='invoice-list-web'),
    path('invoices/create/', InvoiceCreateWebView.as_view(), name='invoice-create'),
    path('invoices/<int:pk>/', InvoiceDetailWebView.as_view(), name='invoice-detail-web'),
    path('invoices/<int:pk>/edit/', InvoiceUpdateWebView.as_view(), name='invoice-edit'),
    path('invoices/<int:pk>/delete/', InvoiceDeleteWebView.as_view(), name='invoice-delete'),
    path('invoices/<int:pk>/print/', InvoicePrintView.as_view(), name='invoice-print'),

    # ============================================================================
    # API ROUTES (REST API Endpoints)
    # ============================================================================
    path('api/invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('api/invoices/<int:pk>/', InvoiceRetrieveUpdateView.as_view(), name='invoice-detail-update'),
    path('api/items/', InvoiceItemListCreateView.as_view(), name='invoice-item-list-create'),
    path('api/items/<int:pk>/', InvoiceItemRetrieveUpdateDestroyView.as_view(), name='invoice-item-detail'),
]