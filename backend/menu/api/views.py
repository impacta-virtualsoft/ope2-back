from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.menu.models import Menu, RecipeMenu, ProductMenu, TypeProductMenu, TypeRecipeMenu
from backend.menu.api.serializers import MenuSerializer, TypeProductMenuSerializer, TypeRecipeMenuSerializer, MenuDetailSerializer, RecipeMenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    http_method_names = [
        "get",
        "post",
        # "patch",
        "delete",
    ]


class TypeProductMenuViewSet(viewsets.ModelViewSet):
    queryset = TypeProductMenu.objects.all()
    serializer_class = TypeProductMenuSerializer
    http_method_names = [
        "get",
        "post",
        # "patch",
        "delete",
    ]


class TypeRecipeMenuViewSet(viewsets.ModelViewSet):
    queryset = TypeRecipeMenu.objects.all()
    serializer_class = TypeRecipeMenuSerializer
    http_method_names = [
        "get",
        "post",
        # "patch",
        "delete",
    ]

class MenuDetailViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuDetailSerializer
    http_method_names = [
        "get",
    ]
