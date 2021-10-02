from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenRefreshSlidingView)
from rest_framework_swagger.views import get_swagger_view

from backend.users.api.views import PermissionsUser

schema_view = get_swagger_view(title='Virtualsoft API')

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    re_path(settings.ADMIN_URL, admin.site.urls),
    # User management
    re_path(r"^users/", include("backend.users.urls", namespace="users")),
    re_path(r"^accounts/", include("allauth.urls")),
    re_path(r'^login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r"^refresh-token/", TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r"^refresh-token-2/", TokenRefreshSlidingView.as_view(), name='token_refresh_2'),
    re_path(r"^swagger/", schema_view),
    re_path(r"^reset_password/", auth_views.PasswordResetView.as_view(), name="reset_password"),
    re_path(r"^reset_password_sent/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    re_path(r"^reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    re_path(r"^reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    re_path(r"^api/", include("config.api_router")),
    # DRF auth token
]

urlpatterns += [
    path("api/user/permission/", PermissionsUser.as_view(), name="permission"),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
