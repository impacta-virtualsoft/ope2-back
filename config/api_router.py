from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from backend.product.api.views import ProductViewSet
from backend.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("product", ProductViewSet)

app_name = "api"
urlpatterns = router.urls
