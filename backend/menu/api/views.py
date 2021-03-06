from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.menu.models import Menu, RecipeMenu, ProductMenu, TypeProductMenu, TypeRecipeMenu
from backend.menu.api.serializers import MenuSerializer, TypeProductMenuSerializer, TypeRecipeMenuSerializer, \
    MenuDetailSerializer, RecipeMenuDetailSerializer, ProductMenuDetailSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    http_method_names = [
        "get",
        "post",
        "patch",
        "delete",
    ]
    filter_backends = [filters.OrderingFilter]


class TypeProductMenuViewSet(viewsets.ModelViewSet):
    queryset = TypeProductMenu.objects.all()
    serializer_class = TypeProductMenuSerializer
    http_method_names = [
        "get",
        "post",
        "patch",
        "delete",
    ]
    filter_backends = [filters.OrderingFilter]


class TypeRecipeMenuViewSet(viewsets.ModelViewSet):
    queryset = TypeRecipeMenu.objects.all()
    serializer_class = TypeRecipeMenuSerializer
    http_method_names = [
        "get",
        "post",
        "patch",
        "delete",
    ]
    filter_backends = [filters.OrderingFilter]

class MenuDetailViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuDetailSerializer
    http_method_names = [
        "get",
    ]
    filter_backends = [filters.OrderingFilter]


class RecipeMenuDetailViewSet(viewsets.ModelViewSet):
    queryset = RecipeMenu.objects.all()
    serializer_class = RecipeMenuDetailSerializer
    http_method_names = [
        "get",
    ]
    filter_backends = [filters.OrderingFilter]


class ProductMenuDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductMenu.objects.all()
    serializer_class = ProductMenuDetailSerializer
    http_method_names = [
        "get",
    ]
    filter_backends = [filters.OrderingFilter]
