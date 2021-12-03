from rest_framework import serializers, status
from rest_framework import fields
from rest_framework.response import Response

from django.db.models import Sum
from backend.core.api.serializers import SmallResultsSetPagination
from backend.menu.models import RecipeMenu, ProductMenu
from backend.order.models import StatusOrder, TypeOrder, SalesOrder, SalesOrderRecipe, SalesOrderProduct


class StatusOrderSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = StatusOrder
        fields = ["id", "name"]


class TypeOrderSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = TypeOrder
        fields = ["id", "name"]


class SalesOrderRecipeSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = SalesOrderRecipe
        fields = ["recipe_menu"]


class SalesOrderProductSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = SalesOrderProduct
        fields = ["product_menu"]


class SalesOrderSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination
    status_order = StatusOrderSerializer(read_only=True)
    total = fields.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    created_in = fields.DateTimeField(read_only=True)
    modified_in = fields.DateTimeField(read_only=True)

    recipe_order = SalesOrderRecipeSerializer(many=True, required=False)
    product_order = SalesOrderProductSerializer(many=True, required=False)

    class Meta:
        model = SalesOrder
        fields = [
            "id", "status_order", "total",
            "client", "comments", "type_order",
            "created_in", "modified_in",
            "recipe_order", "product_order",
        ]
    def create(self, validated_data):
        try:
            recipes_order = validated_data.pop("recipe_order")
        except KeyError:
            recipes_order = ""
        try:
            products_order = validated_data.pop("product_order")
        except KeyError:
            products_order = ""
        order = SalesOrder.objects.create(**validated_data)
        # product_menu = validated_data.pop("product_menu")
        # product = ProductMenu.objects.create(**validated_data)
        if recipes_order:
            for recipe_order in recipes_order:
                try:
                    recipe = RecipeMenu.objects.filter(id=recipe_order["recipe_menu"].id)[0]
                except IndexError:
                    print(123)

                recipe_order_dict = {
                    "recipe_menu": recipe,
                    "sales_order": order,
                }

                SalesOrderRecipe.objects.create(**recipe_order_dict)
            validated_data["recipe_order"] = recipes_order
        if products_order:
            for product_order in products_order:
                try:
                    product = ProductMenu.objects.filter(id=product_order["product_menu"].id)[0]
                except IndexError:
                    print(123)

                product_order_dict = {
                    "product_menu": product,
                    "sales_order": order,
                }

                SalesOrderProduct.objects.create(**product_order_dict)
            validated_data["product_order"] = products_order
        if recipes_order and products_order:
            order.total = SalesOrderRecipe.objects.filter(sales_order=order).aggregate(Sum('recipe_menu__price'))['recipe_menu__price__sum'] + SalesOrderProduct.objects.filter(sales_order=order).aggregate(Sum('product_menu__price'))['product_menu__price__sum']
            order.save()
        elif recipes_order:
            order.total = SalesOrderRecipe.objects.filter(sales_order=order).aggregate(Sum('recipe_menu__price'))['recipe_menu__price__sum']
            order.save()
        elif products_order:
            order.total = SalesOrderProduct.objects.filter(sales_order=order).aggregate(Sum('product_menu__price'))['product_menu__price__sum']
            order.save()
        validated_data["total"] = order.total
        validated_data["status_order"] = order.status_order
        validated_data["id"] = order.id

        return validated_data


class SalesOrderInPreparationSerializer(serializers.ModelSerializer):
    status_order = StatusOrderSerializer(read_only=True)

    class Meta:
        model = SalesOrder
        fields = [
            "id", "status_order"
        ]

    def update(self, instance, validated_data):
        status_order = StatusOrder.objects.get(id=2)
        instance.status_order = status_order
        instance.save()
        return instance


class SalesOrderFinishedSerializer(serializers.ModelSerializer):
    status_order = StatusOrderSerializer(read_only=True)

    class Meta:
        model = SalesOrder
        fields = [
            "id", "status_order"
        ]

    def update(self, instance, validated_data):
        status_order = StatusOrder.objects.get(id=3)
        instance.status_order = status_order
        instance.save()
        return instance


class SalesOrderCanceledSerializer(serializers.ModelSerializer):
    status_order = StatusOrderSerializer(read_only=True)

    class Meta:
        model = SalesOrder
        fields = [
            "id", "status_order"
        ]

    def update(self, instance, validated_data):
        status_order = StatusOrder.objects.get(id=4)
        instance.status_order = status_order
        return instance
