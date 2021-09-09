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
from rest_framework import exceptions, serializers

from backend.users.models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ["username", "name", "email", "password", "groups"]

    def create(self, validated_data):
        create = {
            "username": validated_data["username"],
            "name": validated_data["name"],
            "email": validated_data["email"],
            "password": validated_data["password"],
            "is_staff": True,
        }
        user = User.objects.create(**create)
        group = validated_data["groups"][0]
        user.groups.add(group)
        # user.save()
        serializable_coupon = model_to_dict(user)
        msg = json.dumps(serializable_coupon, indent=4, sort_keys=True, default=str)
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
