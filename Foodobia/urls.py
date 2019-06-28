"""Foodobia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.user import views
from api.meal import meal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.LoginApiView.as_view(), name="login"),
    path('check-user', views.CheckUserName.as_view(), name="check_user"),
    path('signup', views.SignUpApiView.as_view(), name="signup"),
    path('reset-pass', views.ResetPasswordView.as_view(), name="reset_pass"),
    path('list-categories', views.ListCategories.as_view(), name="list_categories"),
    path('choose-categories', meal_views.ListCategoriesApi.as_view(), name="choose_categories"),
    path('user-profile', views.ProfileApi.as_view(), name="list_categories"),
    path('add-category', views.AddCategories.as_view(), name="add_category"),
    path('get-meal', meal_views.GetMealApi.as_view(), name="get_meal")

]























