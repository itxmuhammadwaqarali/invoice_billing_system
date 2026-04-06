from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Sum, Q, Count

# REST API Views
from rest_framework import generics
from .models import Invoice, InvoiceItem
from .serializers import InvoiceSerializer, InvoiceItemSerializer
from rest_framework.permissions import IsAuthenticated

# ============================================================================
# REST API VIEWS (For API Endpoints)
# ============================================================================

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class InvoiceRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]


class InvoiceItemListCreateView(generics.ListCreateAPIView):
    serializer_class = InvoiceItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        invoice_id = self.kwargs.get('invoice_id')
        return InvoiceItem.objects.filter(invoice_id=invoice_id)

    def perform_create(self, serializer):
        invoice_id = self.kwargs.get('invoice_id')
        serializer.save(invoice_id=invoice_id)

class InvoiceItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    permission_classes = [IsAuthenticated]


# ============================================================================
# WEB VIEWS (For Frontend Templates)
# ============================================================================

class DashboardView(LoginRequiredMixin, View):
    """Dashboard showing business overview and statistics"""
    login_url = 'web-login'

    def get(self, request):
        invoices = Invoice.objects.all()
        
        # Calculate statistics
        total_invoices = invoices.count()
        total_paid = invoices.filter(status='paid').aggregate(
            total=Sum('total_amount')
        )['total'] or 0
        total_pending = invoices.exclude(status='paid').aggregate(
            total=Sum('total_amount')
        )['total'] or 0
        total_clients = invoices.values('client').distinct().count()
        
        # Status breakdown
        draft_count = invoices.filter(status='draft').count()
        sent_count = invoices.filter(status='sent').count()
        paid_count = invoices.filter(status='paid').count()
        cancelled_count = invoices.filter(status='cancelled').count()
        total_count = total_invoices or 1
        
        context = {
            'total_invoices': total_invoices,
            'total_paid': total_paid,
            'total_pending': total_pending,
            'total_clients': total_clients,
            'recent_invoices': invoices.order_by('-id')[:10],
            'draft_count': draft_count,
            'sent_count': sent_count,
            'paid_count': paid_count,
            'cancelled_count': cancelled_count,
            'draft_percentage': (draft_count / total_count * 100),
            'sent_percentage': (sent_count / total_count * 100),
            'paid_percentage': (paid_count / total_count * 100),
            'cancelled_percentage': (cancelled_count / total_count * 100),
        }
        return render(request, 'invoices/dashboard.html', context)


class InvoiceListWebView(LoginRequiredMixin, ListView):
    """Display list of all invoices"""
    model = Invoice
    template_name = 'invoices/invoice_list.html'
    context_object_name = 'invoices'
    paginate_by = 20
    login_url = 'web-login'

    def get_queryset(self):
        queryset = Invoice.objects.all().order_by('-id')
        
        # Filter by status
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        
        # Filter by client
        client = self.request.GET.get('client')
        if client:
            queryset = queryset.filter(client__name__icontains=client)
        
        # Filter by invoice number
        invoice = self.request.GET.get('invoice')
        if invoice:
            queryset = queryset.filter(invoice_number__icontains=invoice)
        
        return queryset


class InvoiceDetailWebView(LoginRequiredMixin, DetailView):
    """Display detailed view of a single invoice"""
    model = Invoice
    template_name = 'invoices/invoice_detail.html'
    context_object_name = 'invoice'
    login_url = 'web-login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invoice = self.get_object()
        context['items'] = invoice.items.all()
        return context


class InvoiceCreateWebView(LoginRequiredMixin, CreateView):
    """Create new invoice"""
    model = Invoice
    template_name = 'invoices/invoice_form.html'
    fields = ['client', 'due_date', 'status', 'total_amount', 'tax']
    login_url = 'web-login'

    def get_success_url(self):
        return reverse_lazy('invoice-detail-web', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        from apps.clients.models import Client
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        return context


class InvoiceUpdateWebView(LoginRequiredMixin, UpdateView):
    """Update existing invoice"""
    model = Invoice
    template_name = 'invoices/invoice_form.html'
    fields = ['client', 'due_date', 'status', 'total_amount', 'tax']
    login_url = 'web-login'

    def get_success_url(self):
        return reverse_lazy('invoice-detail-web', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        from apps.clients.models import Client
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['invoice'] = self.get_object()
        return context


class InvoiceDeleteWebView(LoginRequiredMixin, DeleteView):
    """Delete invoice"""
    model = Invoice
    template_name = 'invoices/invoice_confirm_delete.html'
    success_url = reverse_lazy('invoice-list-web')
    login_url = 'web-login'


class InvoicePrintView(LoginRequiredMixin, DetailView):
    """Print-ready invoice view"""
    model = Invoice
    template_name = 'invoices/invoice_print.html'
    context_object_name = 'invoice'
    login_url = 'web-login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invoice = self.get_object()
        context['items'] = invoice.items.all()
        return context

