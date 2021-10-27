from rest_framework import filters, mixins, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.product.api.serializers import (
    ProductDetailSerializer,
    ProductSerializer,
    RecipeSerializer,
    UnitMeasureSerializer,
    TypeProductSerializer,
    RecipeDetailSerializer
)
from backend.product.models import Product, Recipe, UnitMeasure, TypeProduct


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
    serializer_class = ProductDetailSerializer
    http_method_names = ["get"]


class UnitMeasureViewSet(viewsets.ModelViewSet):
    queryset = UnitMeasure.objects.all()
    serializer_class = UnitMeasureSerializer
    http_method_names = [
        "get",
        "post",
        "patch",
        "delete",
    ]


class TypeProductViewSet(viewsets.ModelViewSet):
    queryset = TypeProduct.objects.all()
    serializer_class = TypeProductSerializer
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
        if serializer.is_valid(raise_exception=False) == False:
            dict_product = []
            dict_quantity = []
            for p in serializer.data['recipe_product']:
                dict_product.append(p['product'])
                dict_quantity.append(p['quantity'])
            products = Product.objects.filter(id__in=dict_product, type=0)
            if products:
                for p in products:
                    products_invalid = []
                    products_invalid.append({"id": p.id})
                dict_response = {"error": "Produto não é do tipo Ingrediente","product": products_invalid}
                return Response(
                    dict_response, status=status.HTTP_400_BAD_REQUEST,
                )
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"sucess": "OK"}, status=status.HTTP_200_OK)


class RecipeDetailViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer
    http_method_names = [
        "get",
    ]
    ordering = ("id",)
