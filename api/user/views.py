from api.user.serializers import UserLoginSerializer
from rest_framework.views import APIView
from api.models import users
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.serializers import ValidationError
from django.db.models import Q


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
