import json

from django.contrib.admin.models import (
    ADDITION,
    CHANGE,
    DELETION,
    ContentType,
    LogEntry,
)
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.forms.models import model_to_dict
from rest_framework import exceptions, serializers, pagination

from backend.users.models import User
from backend.core.api.serializers import SmallResultsSetPagination

class GroupSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination
    class Meta:
        model = Group
        fields = ["id", "name"]


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    password = serializers.CharField(write_only=True)
    pagination_class = SmallResultsSetPagination
    ordering = 'id'

    class Meta:
        ordering = "id"
        model = User
        fields = ["id", "first_name", "last_name", "email", "password", "groups"]

    def create(self, validated_data):
        group = validated_data.pop('groups')
        password = validated_data.pop('password')
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.username = validated_data['email']
        user.is_staff = True
        user.save()
        user.groups.add(group[0])
        # user.save()
        serializable_user = model_to_dict(user)
        msg = json.dumps(serializable_user, indent=4, sort_keys=True, default=str)
        LogEntry.objects.log_action(
            user_id=user.id,
            content_type_id=ContentType.objects.get_for_model(
                User, for_concrete_model=False
            ).pk,
            object_id=user.id,
            object_repr="Shopper",
            change_message=msg,
            action_flag=ADDITION,
        )

        return user


class UserDetailSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    pagination_class = SmallResultsSetPagination
    ordering = 'id'

    class Meta:
        ordering = "id"
        model = User
        fields = ["id", "first_name", "last_name", "email", "groups"]
