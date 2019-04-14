from rest_framework.serializers import ModelSerializer
from api.models import users
from django.db.models import Q
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError,
    )


class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = users
        fields = [
            "user_name",
            "user_pass"
        ]

