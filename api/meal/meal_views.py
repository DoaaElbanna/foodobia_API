from api.models import users, Meals, IngredientsCategories, Ingrediants
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.db import connection, transaction
from api.classifier.classifier import predict_diabetes
import numpy as np
import json


cursor = connection.cursor()


def filter_meals(meals_arr):
    arr = []
    for meal in meals_arr:
        arr.append([meal['meal_calories'], meal['meal_fats'], meal['meal_carbs']])

    return arr


def manual_filtering(meals):
        arr = []
        good_arr = []
        for meal in meals:
            if meal['meal_carbs'] <= 50 and meal['meal_carbs'] < 55 * meal['meal_calories'] / 100:
                arr.append(meal)

        for meal in arr:
            if meal['meal_fats'] <= 10:
                good_arr.append(meal)

        return good_arr


def data_splitter(arr):
    if len(arr) % 2 == 0:
        splitted = np.split(arr, 2)
        return splitted[0], splitted[1]
    else:
        middle_index = int(len(arr) / 2)
        splitted = np.split(arr, [middle_index])
        return splitted[0], splitted[1]

    # if len(arr) > 1:
    #     middle_index = int(len(arr) / 2)
    #     arr1 = arr[:middle_index]
    #     arr2 = arr[middle_index:]
    #
    #     return arr1, arr2
    # elif len(arr) == 1:
    #     return arr, []
    # else:
    #     return [], []


class GetMealApi(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data['username']
        user = users.objects.filter(user_name=username).values()
        user_category = tuple(eval(user[0]['fav_category']))
        user_is_diabetic = user[0]['is_diabetic']
        queryset = np.array(Meals.objects.filter(categ_id__in=user_category).values())
        arr1, arr2 = data_splitter(queryset)

        # getting the classified data
        classified_healthy_result = arr1
        if len(arr1) > 0:
            classifier_list = filter_meals(arr1)
            classifier_result = predict_diabetes(classifier_list)
            classified_healthy_result = arr1[classifier_result == 0]

        # get the manual data
        manual_result = arr2
        if len(arr2) > 0:
            manual_result = manual_filtering(arr2)

        if user_is_diabetic == 1:
            return Response(manual_filtering(queryset))
            # return Response(list(manual_result) + list(classified_healthy_result))

        else:
            return Response(queryset)


class ListCategoriesApi(APIView):

    def get(self, request, *args, **kwargs):

        list_categories = IngredientsCategories.objects.all().values()

        final_res = []
        for cat in list_categories:
            sub_categories = np.array(Ingrediants.objects.filter(ingrediant_id__in=tuple(eval(cat['sub_categ']))))
            final_res.append({"categ_name": cat['categ_name'], "sub_categ":  sub_categories})

        return Response(final_res)


class AddNewMealApi(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data['username']
        categ_id = data['categ_id']
        meal_name = data['meal_name']
        meal_img = data['meal_image']
        meal_ingredients = data['meal_ingredients']
        meal_calories = data['meal_calories']
        meal_carbs = data['meal_carbs']
        meal_fats = data['meal_fats']
        meal_protein = data['meal_protein']
        meal_sugar = data['meal_sugar']
        meal_sodium = data['meal_sodium']
        meal_potassium = data['meal_potassium']
        user = users.objects.filter(user_name=username).values()
        user_id = user[0]['user_id']
        # meals_list = list(user[0]['saved_meals'])

        new_meal = Meals(
            meal_name=meal_name,
            meal_image=meal_img,
            meal_ingrediants=meal_ingredients,
            meal_calories=meal_calories,
            meal_carbs=meal_carbs,
            meal_fats=meal_fats,
            meal_protein=meal_protein,
            meal_sugar=meal_sugar,
            meal_sodium=meal_sodium,
            meal_potassium=meal_potassium,
            user=user_id,
            categ=categ_id
        )
        # meals_list.append(new_meal.meal_id)
        # user.update(saved_meals=meals_list)
        return Response({"meal_created": 1})




