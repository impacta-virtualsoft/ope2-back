from django.forms import model_to_dict
from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

from backend.order.models import StatusOrder, TypeOrder, SalesOrder, SalesOrderRecipe, SalesOrderProduct
from backend.order.api.serializers import StatusOrderSerializer, TypeOrderSerializer, SalesOrderSerializer, SalesOrderInPreparationSerializer, SalesOrderFinishedSerializer, SalesOrderCanceledSerializer


class StatusOrderViewSet(viewsets.ModelViewSet):
    queryset = StatusOrder.objects.all()
    serializer_class = StatusOrderSerializer
    http_method_names = [
        "get",
    ]
    filter_backends = [filters.OrderingFilter]


class TypeOrderViewSet(viewsets.ModelViewSet):
    queryset = TypeOrder.objects.all()
    serializer_class = TypeOrderSerializer
    http_method_names = [
        "get",
    ]
    filter_backends = [filters.OrderingFilter]


class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    http_method_names = [
        "get",
        "post",
    ]
    filter_backends = [filters.OrderingFilter]


class SalesOrderInPreparationViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderInPreparationSerializer
    http_method_names = [
        "patch",
    ]
    filter_backends = [filters.OrderingFilter]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.status_order.id == 2:
            return Response({"error": "Pedido já se encontra em preparação"}, status=status.HTTP_400_BAD_REQUEST)
        elif instance.status_order.id > 2:
            return Response({"error": "Pedido já Finalizado ou Cancelado"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)


class SalesOrderFinishedViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderFinishedSerializer
    http_method_names = [
        "patch",
    ]
    filter_backends = [filters.OrderingFilter]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.status_order.id == 3:
            return Response({"error": "Pedido já se encontra Finalizado"}, status=status.HTTP_400_BAD_REQUEST)
        elif instance.status_order.id > 3:
            return Response({"error": "Pedido Cancelado"}, status=status.HTTP_400_BAD_REQUEST)
        elif instance.status_order.id == 1:
            return Response({"error": "Pedido ainda não está em preparação"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)


class SalesOrderCanceledViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderCanceledSerializer
    http_method_names = [
        "patch",
    ]
    filter_backends = [filters.OrderingFilter]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.status_order.id != 4:
            return Response({"error": "Não é possível cancelar um pedido Finalizado"},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
