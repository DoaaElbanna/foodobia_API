from rest_framework.serializers import ModelSerializer
from api.models import FoodCategroies
from django.db.models import Q
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError,
    )


class FoodCategorySerializer(ModelSerializer):
    class Meta:
        model = FoodCategroies
        fields = [
            "categ_id",
            "categ_name",
        ]

