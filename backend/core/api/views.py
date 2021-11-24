from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response

from backend.core.api.serializers import ClientSerializer, ProviderSerializer
from backend.core.models import Client, Provider


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.OrderingFilter]


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = [filters.OrderingFilter]
