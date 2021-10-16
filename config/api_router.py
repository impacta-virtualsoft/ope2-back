from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from backend.core.api.views import ClientViewSet, ProviderViewSet
from backend.product.api.views import (
    ProductDetailViewSet,
    ProductViewSet,
    RecipeViewSet,
    UnitMeasureViewSet,
)
from backend.menu.api.views import MenuViewSet
from backend.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("unitmeasure", UnitMeasureViewSet)
router.register("product", ProductViewSet)
router.register("product/detail", ProductDetailViewSet)
router.register("recipe", RecipeViewSet)
router.register("client", ClientViewSet)
router.register("provider", ProviderViewSet)
router.register("menu", MenuViewSet)

app_name = "api"
urlpatterns = router.urls
