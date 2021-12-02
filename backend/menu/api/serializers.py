from rest_framework import serializers, status, fields
from rest_framework.response import Response

from backend.product.api.serializers import RecipeProductDetailSerializer, ProductDetailSerializer, \
    RecipeDetailSerializer
from backend.product.models import Recipe, Product
from backend.menu.models import Menu, RecipeMenu, ProductMenu, TypeProductMenu, TypeRecipeMenu
from backend.core.api.serializers import SmallResultsSetPagination

class TypeProductMenuSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = TypeProductMenu
        fields = ["id", "name"]


class TypeRecipeMenuSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = TypeRecipeMenu
        fields = ["id", "name",]


class RecipeMenuSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = RecipeMenu
        fields = ["id", "recipe", "type", "price", "status"]


class ProductMenuSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = ProductMenu
        fields = ["id", "product", "type", "price", "status"]


class MenuSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination

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


    def update(self, instance, validated_data):
        recipes_menu = validated_data.get(
            "recipe_menu", instance.recipe_menu
        )
        products_menu = validated_data.get(
            "product_menu", instance.product_menu
        )
        if recipes_menu != instance.recipe_menu:
            RecipeMenu.objects.filter(menu=instance).delete()
            for recipe_menu in recipes_menu:
                recipe_dict = {
                    "menu": instance,
                    "recipe": recipe_menu['recipe'],
                    "type": recipe_menu['type'],
                    "price": recipe_menu['price'],
                    "status": recipe_menu['status'],
                }

                RecipeMenu.objects.create(**recipe_dict)
        if products_menu != instance.product_menu:
            ProductMenu.objects.filter(menu=instance).delete()
            for product_menu in products_menu:
                recipe_dict = {
                    "menu": instance,
                    "product": product_menu['product'],
                    "type": product_menu['type'],
                    "price": product_menu['price'],
                    "status": product_menu['status'],
                }

                ProductMenu.objects.create(**recipe_dict)
        instance.description = validated_data.get("description", instance.description)
        instance.name = validated_data.get("name", instance.name)
        instance.save()

        return instance


class RecipeMenuDetailSerializer(serializers.ModelSerializer):
    price = fields.FloatField
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = RecipeMenu
        fields = ["id", "recipe", "type", "price", "status", "menu"]


class ProductMenuDetailSerializer(serializers.ModelSerializer):
    price = fields.FloatField
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = ProductMenu
        fields = ["id", "product", "type", "price", "status", "menu"]


class MenuDetailSerializer(serializers.ModelSerializer):
    recipe_menu = RecipeMenuDetailSerializer(many=True, required=False)
    product_menu = ProductMenuDetailSerializer(many=True, required=False)
    pagination_class = SmallResultsSetPagination

    class Meta:
        model = Menu
        fields = [
            "id", "name", "description",
            "recipe_menu", "product_menu", "monday",
            "tuesday", "wednesday", "thursday",
            "friday", "saturday", "sunday", "status"
        ]
