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
    groups = serializers.IntegerField
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password", "groups"]

    def create(self, validated_data):
        group = validated_data.pop('groups')
        password = validated_data.pop('password')
        # create = {
        #     "email": validated_data["email"],
        #     "first_name": validated_data["first_name"],
        #     "last_name": validated_data["last_name"],
        #     "is_staff": True,
        # }
        # password = validated_data["password"],
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
