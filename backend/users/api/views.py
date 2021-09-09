from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
# import coreapi
# from rest_framework.schemas import AutoSchema

from backend.users.api.serializers import UserSerializer
from backend.users.models import User

# class UserViewSchema(AutoSchema):
#
#     def get_manual_fields(self, path, method):
#         extra_fields = []
#         if method.lower() in ['post', 'put']:
#             extra_fields = [
#                 coreapi.Field('username')
#             ]
#         manual_fields = super().get_manual_fields(path, method)
#         return manual_fields + extra_fields

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    ordering = ("id",)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class PermissionsUser(APIView):
    def get(self, request, *args, **kwargs):
        groups = self.request.user.groups.first()
        permissions = {}
        for permission in groups.permissions.all():
            authorization = permission.codename.split("_")
            if permissions.get(authorization[1]):
                permissions[authorization[1]].append(authorization[0])
            else:
                permissions[authorization[1]] = []
                permissions[authorization[1]].append(authorization[0])
        return Response(permissions)
