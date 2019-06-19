from rest_framework import serializers
from api.models import Meals


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meals
        fields = '__all__'
        # fields = ['meal_calories', 'meal_carbs', 'meal_fats']


