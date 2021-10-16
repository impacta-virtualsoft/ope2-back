from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.product.api.serializers import (
    ProductDetailsSerializer,
    ProductSerializer,
    RecipeSerializer,
    UnitMeasureSerializer,
)
from backend.product.constants import TYPE_PRODUCT
from backend.product.models import Product, Recipe, UnitMeasure


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = [
        "get",
        "post",
        "patch",
        "delete",
    ]


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    http_method_names = ["get"]


class TypeProduct(APIView):
    def get(self, request, *args, **kwargs):
        type_product = {}
        for a, b in TYPE_PRODUCT:
            type_product[a] = b
        return Response(type_product, status=status.HTTP_200_OK)


class UnitMeasureViewSet(viewsets.ModelViewSet):
    queryset = UnitMeasure.objects.all()
    serializer_class = UnitMeasureSerializer
    http_method_names = [
        "get",
        "post",
        "patch",
        "delete",
    ]


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    http_method_names = [
        "get",
        "post",
        "patch",
        "delete",
    ]
    ordering = ("id",)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"sucess": "OK"}, status=status.HTTP_200_OK)
