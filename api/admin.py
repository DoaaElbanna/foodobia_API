from django.contrib import admin
from .models import (users, Diseases, FoodCategroies, Ingrediants, Meals, ProhibitedMeals)
# Register your models here.

admin.site.register(users)
admin.site.register(Diseases)
admin.site.register(FoodCategroies)
admin.site.register(Ingrediants)
admin.site.register(Meals)
admin.site.register(ProhibitedMeals)
