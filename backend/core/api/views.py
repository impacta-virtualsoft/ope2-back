from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response

from backend.core.api.serializers import ClientSerializer, ProviderSerializer
from backend.core.models import Client, Provider


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.OrderingFilter]

    def create(self, request, *args, **kwargs):
        cpf = request.data.get('cpf', '')
        if cpf and Client.objects.filter(cpf=cpf):
             return Response({"cpf": "Cliente com este CPF já existe."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if request.data.get('cpf', '') and instance.cpf and request.data.get('cpf', '') != instance.cpf:
            return Response({"cpf": "Não é possível alterar o CPF do cliente."}, status=status.HTTP_400_BAD_REQUEST)
        if request.data.get('cpf', '') and Client.objects.filter(cpf=request.data.get('cpf', '')):
            return Response({"cpf": "CPF já cadastrado em outro cliente."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)



class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = [filters.OrderingFilter]
