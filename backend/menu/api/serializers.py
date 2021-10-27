from rest_framework import serializers, status
from rest_framework.response import Response

from backend.product.api.serializers import RecipeProductDetailSerializer, ProductDetailSerializer, \
    RecipeDetailSerializer
from backend.product.models import Recipe, Product
from backend.menu.models import Menu, RecipeMenu, ProductMenu, TypeProductMenu, TypeRecipeMenu
from backend.core.api.serializers import SmallResultsSetPagination

class TypeProductMenuSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination
    ordering = 'id'

    class Meta:
        model = TypeProductMenu
        fields = ["id", "name"]


class TypeRecipeMenuSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination
    ordering = 'id'

    class Meta:
        model = TypeRecipeMenu
        fields = ["id", "name",]


class RecipeMenuSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination
    ordering = 'id'

    class Meta:
        model = RecipeMenu
        fields = ["recipe", "type", "price", "status"]


class ProductMenuSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination
    ordering = 'id'

    class Meta:
        model = ProductMenu
        fields = ["product", "type", "price", "status"]


class MenuSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination
    ordering = 'id'

    recipe_menu = RecipeMenuSerializer(many=True, required=False)
    product_menu = ProductMenuSerializer(many=True, required=False)

    class Meta:
        model = Menu
        fields = [
            "id", "name", "description",
            "recipe_menu", "product_menu", "monday",
            "tuesday", "wednesday", "thursday",
            "friday", "saturday", "sunday", "status"
        ]
    def create(self, validated_data):
        try:
            recipes_menu = validated_data.pop("recipe_menu")
        except KeyError:
            recipes_menu = ""
        try:
            products_menu = validated_data.pop("product_menu")
        except KeyError:
            products_menu = ""
        menu = Menu.objects.create(**validated_data)
        # product_menu = validated_data.pop("product_menu")
        # product = ProductMenu.objects.create(**validated_data)
        if recipes_menu:
            for recipe_menu in recipes_menu:
                try:
                    recipe = Recipe.objects.filter(id=recipe_menu["recipe"].id)[0]
                except IndexError:
                    print(123)

                recipe_menu_dict = {
                    "recipe": recipe,
                    "menu": menu,
                    "type": recipe_menu["type"],
                    "price": recipe_menu["price"],
                    "status": recipe_menu["status"],
                }

                RecipeMenu.objects.create(**recipe_menu_dict)
            validated_data["recipe_menu"] = recipes_menu
        if products_menu:
            for product_menu in products_menu:
                try:
                    product = Product.objects.filter(id=product_menu["product"].id)[0]
                except IndexError:
                    print(123)

                product_menu_dict = {
                    "product": product,
                    "menu": menu,
                    "type": product_menu["type"],
                    "price": product_menu["price"],
                    "status": product_menu["status"],
                }

                ProductMenu.objects.create(**product_menu_dict)
            validated_data["product_menu"] = products_menu
        validated_data["id"] = menu.id

        return validated_data

class RecipeMenuDetailSerializer(serializers.ModelSerializer):
    recipe = RecipeDetailSerializer(many=False)
    type = TypeRecipeMenuSerializer(many=False, read_only=True)
    pagination_class = SmallResultsSetPagination
    ordering = 'id'

    class Meta:
        model = RecipeMenu
        fields = ["recipe", "type", "price", "status"]


class ProductMenuDetailSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(many=False)
    type = TypeProductMenuSerializer(many=False)
    pagination_class = SmallResultsSetPagination
    ordering = 'id'

    class Meta:
        model = ProductMenu
        fields = ["product", "type", "price", "status"]


class MenuDetailSerializer(serializers.ModelSerializer):
    recipe_menu = RecipeMenuDetailSerializer(many=True, required=False)
    product_menu = ProductMenuDetailSerializer(many=True, required=False)
    pagination_class = SmallResultsSetPagination
    ordering = 'id'

    class Meta:
        model = Menu
        fields = [
            "id", "name", "description",
            "recipe_menu", "product_menu", "monday",
            "tuesday", "wednesday", "thursday",
            "friday", "saturday", "sunday", "status"
        ]
