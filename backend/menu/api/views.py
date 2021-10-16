from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.menu.models import Menu, RecipeMenu, ProductMenu
from backend.menu.api.serializers import MenuSerializer, RecipeMenuSerializer, ProductMenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    http_method_names = [
        "get",
        "post",
        # "patch",
        "delete",
    ]
