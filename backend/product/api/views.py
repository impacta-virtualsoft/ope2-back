from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from backend.product.api.serializers import ProductSerializer
from backend.product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        This view should return a list
        for the currently authenticated user.
        """
        user = self.request.user
        #

        if user.is_cashier():
            return self.queryset
