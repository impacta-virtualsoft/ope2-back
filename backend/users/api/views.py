from rest_framework import status, viewsets, permissions
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
    # permission_classes = (permissions.Is)
    ordering = ("id",)

    # list(self, request), create(self, request), update(self, request, pk=None), destroy(self, request, pk=None)
    # retrieve(self, request, pk=None) "GET COM ID", partial_update(self, request, pk=None),

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_owner():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response({'error': 'Unauthorized'},status=status.HTTP_401_UNAUTHORIZED)

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_owner():
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(
                serializer.data, status=status.HTTP_200_OK
            )
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


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
