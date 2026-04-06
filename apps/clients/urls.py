from django.urls import path

from apps.clients.views import ClientDetailView, ClientListCreateView

urlpatterns = [
    path('', ClientListCreateView.as_view(), name='client-list-create'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
]
