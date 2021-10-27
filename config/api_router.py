from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from backend.core.api.views import ClientViewSet, ProviderViewSet
from backend.product.api.views import (
    ProductDetailViewSet,
    ProductViewSet,
    RecipeViewSet,
    RecipeDetailViewSet,
    UnitMeasureViewSet,
    TypeProductViewSet,
)
from backend.menu.api.views import MenuViewSet, MenuDetailViewSet,TypeProductMenuViewSet, TypeRecipeMenuViewSet
from backend.users.api.views import UserViewSet, UserDetailViewSet

router = DefaultRouter()

router.register("users", UserViewSet)
router.register("users-detail", UserDetailViewSet)
router.register("unitmeasure", UnitMeasureViewSet)
router.register("product/type", TypeProductViewSet)
router.register("product", ProductViewSet)
router.register("product-detail", ProductDetailViewSet)
router.register("recipe", RecipeViewSet)
router.register("recipe-detail", RecipeDetailViewSet)
router.register("client", ClientViewSet)
router.register("provider", ProviderViewSet)
router.register("menu", MenuViewSet)
router.register("menu-detail", MenuDetailViewSet)
router.register("menu-typeproduct", TypeProductMenuViewSet)
router.register("menu-typerecipe", TypeRecipeMenuViewSet)

app_name = "api"
urlpatterns = router.urls
