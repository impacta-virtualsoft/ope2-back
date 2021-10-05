from rest_framework import mixins, status, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.product.api.serializers import ProductSerializer, ProductDetailsSerializer, UnitMeasureSerializer, RevenueSerializer, RevenueProductSerializer, RevenueProductDetailSerializer
from backend.product.models import Product, UnitMeasure, Revenue, RevenueProduct
from backend.product.constants import TYPE_PRODUCT


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    http_method_names = ['get']

class TypeProduct(APIView):
    def get(self, request, *args, **kwargs):
        type_product = {}
        for a, b in TYPE_PRODUCT:
            type_product[a] = b
        return Response(type_product,status=status.HTTP_200_OK)


class UnitMeasureViewSet(viewsets.ModelViewSet):
    queryset = UnitMeasure.objects.all()
    serializer_class = UnitMeasureSerializer


class RevenueViewSet(viewsets.ModelViewSet):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer


class RevenueProductViewSet(viewsets.ModelViewSet):
    queryset = RevenueProduct.objects.all()
    serializer_class = RevenueProductSerializer

class RevenueProductDetailViewSet(viewsets.ModelViewSet):
    queryset = RevenueProduct.objects.all()
    serializer_class = RevenueProductDetailSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('id',)
    http_method_names = ['get']
    lookup_field = 'id'
