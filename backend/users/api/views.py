from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.users.models import User
from backend.users.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    ordering = ('id',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PermissionsUser(APIView):
    def get(self, request, *args, **kwargs):
        groups = self.request.user.groups.first()
        permissions = {}
        for permission in groups.permissions.all():
            authorization = permission.codename.split('_')
            if permissions.get(authorization[1]):
                permissions[authorization[1]].append(authorization[0])
            else:
                permissions[authorization[1]] = []
                permissions[authorization[1]].append(authorization[0])
        return Response(permissions)
