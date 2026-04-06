# 🔗 Complete URL Mapping Guide

## ✅ All URLs Configured!

Here's the complete URL structure for your invoice billing system with both web pages and API endpoints.

---

## 🌐 WEB ROUTES (Frontend Pages)

### Dashboard
- **URL**: `/`
- **Name**: `dashboard`
- **View**: `DashboardView`
- **Method**: GET
- **Template**: `invoices/dashboard.html`
- **Authentication**: Required (LoginRequired)
- **Description**: Show business overview with statistics

```
http://yoursite.com/
```

---

### Invoice List (Web)
- **URL**: `/invoices/`
- **Name**: `invoice-list-web`
- **View**: `InvoiceListWebView`
- **Method**: GET
- **Template**: `invoices/invoice_list.html`
- **Authentication**: Required
- **Filters**: status, client, invoice
- **Description**: Display all invoices with filtering and pagination

```
http://yoursite.com/invoices/
http://yoursite.com/invoices/?status=paid
http://yoursite.com/invoices/?client=Acme
http://yoursite.com/invoices/?invoice=INV001
```

---

### Create Invoice
- **URL**: `/invoices/create/`
- **Name**: `invoice-create`
- **View**: `InvoiceCreateWebView`
- **Methods**: GET (form), POST (submit)
- **Template**: `invoices/invoice_form.html`
- **Authentication**: Required
- **Description**: Create a new invoice

```
GET:  http://yoursite.com/invoices/create/       (Show form)
POST: http://yoursite.com/invoices/create/       (Create invoice)
```

---

### Invoice Detail (Web)
- **URL**: `/invoices/<int:pk>/`
- **Name**: `invoice-detail-web`
- **View**: `InvoiceDetailWebView`
- **Methods**: GET
- **Template**: `invoices/invoice_detail.html`
- **Authentication**: Required
- **URL Parameters**: pk (invoice ID)
- **Description**: View full invoice details with items

```
http://yoursite.com/invoices/1/
http://yoursite.com/invoices/5/
```

---

### Edit Invoice
- **URL**: `/invoices/<int:pk>/edit/`
- **Name**: `invoice-edit`
- **View**: `InvoiceUpdateWebView`
- **Methods**: GET (form), POST (submit)
- **Template**: `invoices/invoice_form.html`
- **Authentication**: Required
- **URL Parameters**: pk (invoice ID)
- **Description**: Edit existing invoice

```
GET:  http://yoursite.com/invoices/1/edit/       (Show form)
POST: http://yoursite.com/invoices/1/edit/       (Update invoice)
```

---

### Delete Invoice
- **URL**: `/invoices/<int:pk>/delete/`
- **Name**: `invoice-delete`
- **View**: `InvoiceDeleteWebView`
- **Methods**: GET (confirmation), POST (delete)
- **Template**: `invoices/invoice_confirm_delete.html`
- **Authentication**: Required
- **URL Parameters**: pk (invoice ID)
- **Description**: Delete invoice with confirmation

```
GET:  http://yoursite.com/invoices/1/delete/     (Show confirmation)
POST: http://yoursite.com/invoices/1/delete/     (Delete invoice)
```

---

### Print Invoice
- **URL**: `/invoices/<int:pk>/print/`
- **Name**: `invoice-print`
- **View**: `InvoicePrintView`
- **Method**: GET
- **Template**: `invoices/invoice_print.html`
- **Authentication**: Required
- **URL Parameters**: pk (invoice ID)
- **Description**: Print-ready invoice (can save as PDF)

```
http://yoursite.com/invoices/1/print/
```

---

## 🔌 API ROUTES (REST Endpoints)

### Invoice List & Create (API)
- **URL**: `/api/invoices/`
- **Name**: `invoice-list-create`
- **View**: `InvoiceListCreateView`
- **Methods**: 
  - GET: List all invoices
  - POST: Create new invoice
- **Authentication**: Token/JWT Required
- **Response**: JSON

```
GET:  http://yoursite.com/api/invoices/
POST: http://yoursite.com/api/invoices/
```

**POST Request Example:**
```json
{
    "client": 1,
    "due_date": "2026-05-15",
    "status": "draft",
    "total_amount": 1000.00,
    "tax": 10
}
```

---

### Invoice Detail, Update, Delete (API)
- **URL**: `/api/invoices/<int:pk>/`
- **Name**: `invoice-detail-update`
- **View**: `InvoiceRetrieveUpdateView`
- **Methods**:
  - GET: Retrieve invoice
  - PUT: Full update
  - PATCH: Partial update
- **Authentication**: Token/JWT Required
- **Response**: JSON

```
GET:    http://yoursite.com/api/invoices/1/
PUT:    http://yoursite.com/api/invoices/1/
PATCH:  http://yoursite.com/api/invoices/1/
```

**PATCH Request Example (Update Status):**
```json
{
    "status": "paid"
}
```

---

### Invoice Items List & Create (API)
- **URL**: `/api/invoices/<int:invoice_id>/items/`
- **Name**: `invoice-item-list-create`
- **View**: `InvoiceItemListCreateView`
- **Methods**:
  - GET: List items for invoice
  - POST: Create new item
- **Authentication**: Token/JWT Required
- **URL Parameters**: invoice_id
- **Response**: JSON

```
GET:  http://yoursite.com/api/invoices/1/items/
POST: http://yoursite.com/api/invoices/1/items/
```

**POST Request Example:**
```json
{
    "description": "Web Design",
    "quantity": 5,
    "unit_price": 500.00,
    "total_price": 2500.00
}
```

---

### Invoice Item Detail, Update, Delete (API)
- **URL**: `/api/items/<int:pk>/`
- **Name**: `invoice-item-detail`
- **View**: `InvoiceItemRetrieveUpdateDestroyView`
- **Methods**:
  - GET: Retrieve item
  - PUT: Full update
  - PATCH: Partial update
  - DELETE: Delete item
- **Authentication**: Token/JWT Required
- **URL Parameters**: pk (item ID)
- **Response**: JSON

```
GET:    http://yoursite.com/api/items/1/
PUT:    http://yoursite.com/api/items/1/
PATCH:  http://yoursite.com/api/items/1/
DELETE: http://yoursite.com/api/items/1/
```

---

## 📋 Quick Reference Table

| Purpose | URL | Name | Method | Type |
|---------|-----|------|--------|------|
| Dashboard | `/` | `dashboard` | GET | Web |
| List Invoices | `/invoices/` | `invoice-list-web` | GET | Web |
| Create Invoice | `/invoices/create/` | `invoice-create` | GET/POST | Web |
| View Invoice | `/invoices/<id>/` | `invoice-detail-web` | GET | Web |
| Edit Invoice | `/invoices/<id>/edit/` | `invoice-edit` | GET/POST | Web |
| Delete Invoice | `/invoices/<id>/delete/` | `invoice-delete` | GET/POST | Web |
| Print Invoice | `/invoices/<id>/print/` | `invoice-print` | GET | Web |
| API - List | `/api/invoices/` | `invoice-list-create` | GET/POST | API |
| API - Detail | `/api/invoices/<id>/` | `invoice-detail-update` | GET/PUT/PATCH | API |
| API - Items | `/api/invoices/<id>/items/` | `invoice-item-list-create` | GET/POST | API |
| API - Item | `/api/items/<id>/` | `invoice-item-detail` | GET/PUT/PATCH/DELETE | API |

---

## 🎯 Usage in Templates

### Using URL Names in Templates

Instead of hardcoding URLs, use Django's `{% url %}` tag:

```html
<!-- Dashboard Link -->
<a href="{% url 'dashboard' %}">Dashboard</a>

<!-- Invoice List Link -->
<a href="{% url 'invoice-list-web' %}">All Invoices</a>

<!-- Create Invoice Link -->
<a href="{% url 'invoice-create' %}">Create Invoice</a>

<!-- View Invoice Link (with parameter) -->
<a href="{% url 'invoice-detail-web' invoice.id %}">View Invoice</a>

<!-- Edit Invoice Link -->
<a href="{% url 'invoice-edit' invoice.id %}">Edit</a>

<!-- Delete Invoice Link -->
<a href="{% url 'invoice-delete' invoice.id %}">Delete</a>

<!-- Print Invoice Link -->
<a href="{% url 'invoice-print' invoice.id %}">Print</a>
```

### Using URL Names in Views

```python
from django.urls import reverse

# In a view
url = reverse('invoice-detail-web', kwargs={'pk': invoice.id})

# In a form
return redirect('invoice-detail-web', pk=self.object.id)
```

---

## 🔐 Authentication

### Web Routes
- **Required**: Django LoginRequiredMixin
- **Redirects To**: `login` URL (must be configured in settings)
- **Login URL**: Add to `settings.py`:
  ```python
  LOGIN_URL = 'login'  # Or your login URL name
  ```

### API Routes
- **Required**: REST Framework Token or JWT Authentication
- **Headers**: Add to requests:
  ```
  Authorization: Token YOUR_TOKEN_HERE
  ```

---

## 🧪 Testing URLs

### Using cURL (Command Line)

**Get Dashboard:**
```bash
curl http://yoursite.com/
```

**List Invoices (API):**
```bash
curl -H "Authorization: Token YOUR_TOKEN" http://yoursite.com/api/invoices/
```

**Create Invoice (API):**
```bash
curl -X POST http://yoursite.com/api/invoices/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "client": 1,
    "due_date": "2026-05-15",
    "status": "draft",
    "total_amount": 1000.00,
    "tax": 10
  }'
```

---

## 📝 URL Configuration File

Here's what's in your `apps/invoices/urls.py`:

```python
# Web Routes (Frontend)
path('', DashboardView.as_view(), name='dashboard')
path('invoices/', InvoiceListWebView.as_view(), name='invoice-list-web')
path('invoices/create/', InvoiceCreateWebView.as_view(), name='invoice-create')
path('invoices/<int:pk>/', InvoiceDetailWebView.as_view(), name='invoice-detail-web')
path('invoices/<int:pk>/edit/', InvoiceUpdateWebView.as_view(), name='invoice-edit')
path('invoices/<int:pk>/delete/', InvoiceDeleteWebView.as_view(), name='invoice-delete')
path('invoices/<int:pk>/print/', InvoicePrintView.as_view(), name='invoice-print')

# API Routes (REST)
path('api/invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create')
path('api/invoices/<int:pk>/', InvoiceRetrieveUpdateView.as_view(), name='invoice-detail-update')
path('api/invoices/<int:invoice_id>/items/', InvoiceItemListCreateView.as_view(), name='invoice-item-list-create')
path('api/items/<int:pk>/', InvoiceItemRetrieveUpdateDestroyView.as_view(), name='invoice-item-detail')
```

---

## ✅ Complete! 

All URLs are configured and ready to use! 🎉

- ✅ 7 Web routes for frontend
- ✅ 4 API routes for REST endpoints
- ✅ URL names for easy reference
- ✅ Authentication configured
- ✅ All templates updated with correct URLs

