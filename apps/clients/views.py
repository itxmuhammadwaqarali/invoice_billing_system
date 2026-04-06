from rest_framework import generics

from apps.clients.models import Client
from apps.clients.serializers import ClientSerializer


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all().order_by('-created_at')
    serializer_class = ClientSerializer


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
