from rest_framework.views import APIView
from api.models import users, FoodCategroies
from rest_framework.response import Response
from rest_framework import generics
from .serializers import FoodCategorySerializer
from django.core.mail import send_mail
from django.conf import  settings
from django.contrib.auth.models import User


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

    def post(self,request,*args,**kwargs):
        data = request.data
        username = data["username"]
        usr_email = list(data["email"] ) # user@gmail.com
        password = User.objects.make_random_password()
       # user= users.set_password(password)

        user = users.objects.filter(user_name=username).update(user_pass=password)
        subject='Foodobia password recover'
        message = "This is your new password: " + password
        email_from = settings.Email_Host_USER
        #to_list=[settings.EMAIL_HOST_USER]
        email_res = send_mail(subject, message, email_from, usr_email, fail_silently=True)
        if(email_res):
            return Response({"msg": 1})
        else:
            return Response({"msg": 0})


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
