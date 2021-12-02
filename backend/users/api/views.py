from rest_framework import filters, status, viewsets
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.users.api.serializers import UserSerializer, UserDetailSerializer, ChangePasswordSerializer
from backend.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.Is)
    filter_backends = [filters.OrderingFilter]

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
            return Response(
                {"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
            )

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_owner():
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
            )

class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    http_method_names = ['get']
    filter_backends = [filters.OrderingFilter]

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_owner():
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
            )

class PermissionsUser(APIView):
    # filter_backends = [filters.OrderingFilter, SmallResultsSetPagination]
    def get(self, request, *args, **kwargs):
        groups = self.request.user.groups.first()
        dict_permission = {"user_email": self.request.user.email, "permissions": []}
        for permission in groups.permissions.all():
            authorization = permission.codename.split("_")
            try:
                if dict_permission["permissions"][-1].get("area") == authorization[1]:
                    dict_permission["permissions"][-1]["actions"].append(
                        authorization[0]
                    )
                else:
                    dict_permission["permissions"].append(
                        {"area":authorization[1], "actions":[authorization[0]]}
                    )
            except IndexError:
                dict_permission["permissions"].append(
                    {"area":authorization[1], "actions":[authorization[0]]}
                )
        return Response(dict_permission)


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
