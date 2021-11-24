from django.forms.models import model_to_dict
from rest_framework import serializers, status
from rest_framework.response import Response

from backend.product.models import Product, Recipe, RecipeProduct, UnitMeasure, TypeProduct
from backend.core.api.serializers import SmallResultsSetPagination


class UnitMeasureSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = UnitMeasure
        fields = [
            "id",
            "name",
            "short_name",
        ]


class TypeProductSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = TypeProduct
        fields = [
            "id",
            "name",
        ]


class ProductSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination
    class Meta:
        model = Product
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):
    unit_measure = UnitMeasureSerializer(many=False, read_only=True)
    type = TypeProductSerializer(many=False, read_only=True)
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "type",
            "unit_measure",
        ]


class RecipeProductSerializer(serializers.ModelSerializer):
    quantity = serializers.DecimalField(max_digits=10, decimal_places=2)
    # product = serializers.IntegerField()
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = RecipeProduct
        fields = ["product", "quantity"]


class RecipeSerializer(serializers.ModelSerializer):
    recipe_product = RecipeProductSerializer(many=True)
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "description",
            "recipe_product",
        ]

    def create(self, validated_data):
        recipe_products = validated_data.pop("recipe_product")
        recipe = Recipe.objects.create(**validated_data)

        for recipe_product in recipe_products:
            try:
                product = Product.objects.filter(id=recipe_product["product"].id)[0]
            except IndexError:
                print(123)

            recipe_dict = {
                "recipe": recipe,
                "product": product,
                "quantity": recipe_product["quantity"],
            }

            RecipeProduct.objects.create(**recipe_dict)

        validated_data["recipe_product"] = recipe_products
        validated_data["id"] = recipe.id

        return validated_data

    def update(self, instance, validated_data):
        recipe_products = validated_data.get(
            "recipe_product", instance.recipe_product
        )
        if recipe_products != instance.recipe_product:
            RecipeProduct.objects.filter(recipe=instance).delete()
            for recipe_product in recipe_products:
                product = Product.objects.filter(id=recipe_product["product"].id)[0]
                recipe_dict = {
                    "recipe": instance,
                    "product": product,
                    "quantity": recipe_product["quantity"],
                }

                RecipeProduct.objects.create(**recipe_dict)
        instance.description = validated_data.get("description", instance.description)
        instance.name = validated_data.get("name", instance.name)
        instance.save()

        return instance


class RecipeProductDetailSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(many=False)
    quantity = serializers.DecimalField(max_digits=10, decimal_places=2)
    # product = serializers.IntegerField()
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = RecipeProduct
        fields = ["product", "quantity"]


class RecipeDetailSerializer(serializers.ModelSerializer):
    recipe_product = RecipeProductDetailSerializer(many=True)
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "description",
            "recipe_product",
        ]
