from rest_framework import serializers, status
from rest_framework.response import Response

from django.forms.models import model_to_dict

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
        fields = ['product','quantity']

class RevenueSerializer(serializers.ModelSerializer):
    revenue_product = RevenueProductSerializer(many=True)
    class Meta:
        model = Revenue
        fields = [
            'id',
            'description',
            'revenue_product',
        ]

    def create(self, validated_data):
        revenue_products = validated_data.pop('revenue_product')
        revenue = Revenue.objects.create(**validated_data)

        rp_list = []
        for revenue_product in revenue_products:
            try:
                product = Product.objects.filter(id=revenue_product['product'].id)[0]
            except IndexError:
                print(123)

            revenue_dict = {
                "revenue":revenue,
                "product": product,
                "quantity": revenue_product['quantity'],
            }

            RevenueProduct.objects.create(**revenue_dict)

        validated_data['revenue_product'] = revenue_products
        validated_data['id'] = revenue.id

        return validated_data

    def update(self, instance, validated_data):
        revenue_products = validated_data.get("revenue_product", instance.revenue_product)
        if revenue_products != instance.revenue_product:
            RevenueProduct.objects.filter(revenue=instance).delete()
            for revenue_product in revenue_products:
                product = Product.objects.filter(id=revenue_product['product'].id)[0]
                revenue_dict = {
                    "revenue": instance,
                    "product": product,
                    "quantity": revenue_product['quantity'],
                }

                RevenueProduct.objects.create(**revenue_dict)
        instance.description = validated_data.get("description", instance.description)
        instance.save()

        return instance

# class RevenueProductDetailSerializer(serializers.ModelSerializer):
#     # revenue = RevenueSerializer(many=False)
#     # product = ProductDetailsSerializer(many=True)
#
#     class Meta:
#         model = RevenueProduct
#         fields = "__all__"
