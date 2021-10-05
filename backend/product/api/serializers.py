from rest_framework import serializers

from backend.product.models import Product, UnitMeasure, Revenue, RevenueProduct
from backend.product.constants import INGREDIENT, TYPE_PRODUCT

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UnitMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitMeasure
        fields = [
            'id',
            'description',
            'short_description',
        ]


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = [
            'id',
            'description',
        ]


class ProductDetailsSerializer(serializers.ModelSerializer):
    unit_measure = UnitMeasureSerializer(many=False)
    type = serializers.ChoiceField(choices=TYPE_PRODUCT)
    class Meta:
        ordering = ['id']
        model = Product
        fields = [
            'id',
            'description',
            'type',
            'unit_measure',
        ]


class RevenueProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueProduct
        fields = "__all__"


class RevenueProductDetailSerializer(serializers.ModelSerializer):
    revenue = RevenueSerializer(many=False)
    product = ProductDetailsSerializer(many=True)

    class Meta:
        model = RevenueProduct
        fields = [
            'id',
            'revenue',
            'product',
            'quantity'
        ]

    def get_serialized(self, id):
        queryset = RevenueProduct.objects.filter(id=id)
        serializers=RevenueProductDetailSerializer(queryset, many=True)
        data = serializers.data
        return data
