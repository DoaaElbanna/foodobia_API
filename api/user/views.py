from rest_framework.views import APIView
from api.models import users, FoodCategroies
from rest_framework.response import Response
from rest_framework import generics
from .serializers import FoodCategorySerializer
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
import json


class LoginApiView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data["username"]
        password = data["password"]
        user = users.objects.filter(user_name=username, user_pass=password)
        if user.exists() and user.count() == 1:
            user_obj = 1  # if username exist
        else:
            user_obj = 0  # if username does not exist

        res = {"auth": user_obj}

        return Response(res)


class ResetPasswordView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data["username"]
        user = users.objects.filter(user_name=username).values()
        user_email = user[0]['user_email']
        user_password = user[0]['user_pass']
        subject = 'Foodobia password recover'
        message = "This is your password: " + user_password
        email = EmailMessage(
            subject, message, to=[user_email]
        )
        email_res = email.send()
        if email_res:
            return Response({"password_send": email_res})  # pass send
        else:
            return Response({"password_send": email_res})  # pass not send


class CheckUserName(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data["username"]
        user = users.objects.filter(user_name=username)
        if user.exists():
            user_object = 1
            # this user already exist
        else:
            user_object = 0  # this user not exist

        res = {"exist": user_object}
        return Response(res)


class SignUpApiView(APIView):

    def post(self, request, *arg, **kwargs):
        data = request.data
        username = data["username"]
        password = data["password"]
        first_name = data["firstName"]
        last_name = data["lastName"]
        email = data["email"]
        birth_data = data["birthData"]
        gender = data["gender"]
        phone_number = data["phoneNumber"]
        length = data["length"]
        weight = data["weight"]
        is_diabetic = data["isDiabetic"]

        new_user = users(
            user_name=username,
            user_email=email,
            user_firstname=first_name,
            user_lastname=last_name,
            user_pass=password,
            user_birthdate=birth_data,
            user_gender=gender,
            user_phone=phone_number,
            user_length=length,
            user_weight=weight,
            is_diabetic=is_diabetic,
        )
        new_user.save()
        res = {"created": 1}
        return Response(res)


class ListCategories(generics.ListAPIView):  # return array of objects from Food categories
    queryset = FoodCategroies.objects.all()
    serializer_class = FoodCategorySerializer


class AddCategories(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data["username"]
        categories_list = data["categ_id"]
        user = users.objects.filter(user_name=username).update(fav_category=categories_list)
        res = {"updated": 1}
        return Response(res)


class ProfileApi(APIView):

    def post(self, request):
        data = request.data
        username = data["username"]
        user = users.objects.filter(user_name=username).values()
        username = user[0]['user_name']
        firstname = user[0]['user_firstname']
        lastname = user[0]['user_lastname']
        # image = user[0]['user_image']
        email = user[0]['user_email']
        length = user[0]['user_length']
        weight = user[0]['user_weight']
        saved_meal = user[0]['saved_meals']
        fav_category = user[0]['fav_category']
        categories_list = FoodCategroies.objects.filter(categ_id__in=tuple(eval(fav_category))).values()
        categories_name = []

        for cat in categories_list:
            categories_name.append(cat['categ_name'])

        user_profile = [{"username":username, "firstname": firstname, "lastname": lastname,
                         "email": email, "length": length, "weight": weight, "saved+meal": saved_meal,
                         "fav_category": categories_name}]

        return Response(user_profile)