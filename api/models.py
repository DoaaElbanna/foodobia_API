# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django_mysql.models import JSONField
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class users(models.Model):
    user_id = models.AutoField(db_column='user-id', primary_key=True)
    gmail_id = models.BigIntegerField(db_column='gmail-id', blank=True, null=True)
    user_name = models.CharField(db_column='user-name', unique=True, max_length=45, blank=True, null=True)
    user_firstname = models.CharField(db_column='user-firstname', max_length=45, blank=True, null=True)
    user_lastname = models.CharField(db_column='user-lastname', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_image = models.TextField(db_column='user-image', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_pass = models.CharField(db_column='user-pass', max_length=255)  # Field renamed to remove unsuitable characters.
    user_email = models.CharField(db_column='user-email', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_birthdate = models.DateField(db_column='user-birthdate', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_phone = models.IntegerField(db_column='user-phone', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_gender = models.IntegerField(db_column='user-gender', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_length = models.IntegerField(db_column='user-length', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_weight = models.IntegerField(db_column='user-weight', blank=True, null=True)   # Field renamed to remove unsuitable characters.
    user_activitylevel = models.IntegerField(db_column='user-activitylevel', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    is_diabetic = models.IntegerField(db_column='is-diabetic', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fav_category = models.TextField(db_column='fav-category', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    saved_meals = models.TextField(db_column='saved-meals', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        # managed = False
        db_table = 'users'


class Diseases(models.Model):
    disease_id = models.AutoField(db_column='disease-id', primary_key=True)  # Field renamed to remove unsuitable characters.
    disease_name = models.TextField(db_column='disease-name', blank=True, null=True)
    users_user_id = models.ForeignKey('Users', models.DO_NOTHING, db_column='users_user-id', null=True)

    class Meta:
        # managed = False
        db_table = 'diseases'


class FoodCategroies(models.Model):
    categ_id = models.AutoField(db_column='categ-id', primary_key=True)  # Field renamed to remove unsuitable characters.
    categ_name = models.CharField(db_column='categ-name', max_length=45, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'food_categroies'


class Ingrediants(models.Model):
    ingrediant_id = models.AutoField(db_column='ingrediants-id', primary_key=True)
    ingrediant_name = models.CharField(db_column='ingrediants-name', max_length=45, blank=True, null=True)
    carbs = models.FloatField(blank=True, null=True)
    fats = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    sugar = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)
    potassium = models.FloatField(blank=True, null=True)
    is_countable = models.IntegerField(db_column='is-countable')  # Field renamed to remove unsuitable characters.

    class Meta:
        # managed = False
        db_table = 'ingrediants'

# class IngrediantsHasDiseases(models.Model):
#     ingrediants_ingrediants_id = models.ForeignKey(Ingrediants, models.DO_NOTHING,
#                                                    db_column='ingrediants_ingrediants-id', primary_key=True)
#     diseases_id_diseases = models.ForeignKey(Diseases, models.DO_NOTHING, db_column='diseases_id-diseases')
#
#
#     class Meta:
#         managed = False
#         db_table = 'ingrediants_has_diseases'
#         unique_together = (('ingrediants_ingrediants_id', 'diseases_id_diseases'),)


class IngredientsCategories(models.Model):
    categ_id = models.AutoField(primary_key=True)
    categ_name = models.CharField(max_length=45, blank=True, null=True)
    sub_categ = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients_categories'


class Meals(models.Model):
    meal_id = models.AutoField(db_column='meal-id', primary_key=True)
    meal_name = models.CharField(db_column='meal-name', unique=True, max_length=45, blank=True, null=True)
    meal_image = models.TextField(db_column='meal-image', blank=True, null=True)
    meal_ingrediants = models.TextField(db_column='meal-ingrediants', blank=True, null=True)
    meal_calories = models.FloatField(db_column='meal-calories', blank=True, null=True)
    meal_carbs = models.FloatField(db_column='meal-carbs', blank=True, null=True)
    meal_fats = models.FloatField(db_column='meal-fats', blank=True, null=True)
    meal_protein = models.FloatField(db_column='meal-protein', blank=True, null=True)
    meal_sugar = models.FloatField(db_column='meal-sugar', blank=True, null=True)
    meal_sodium = models.FloatField(db_column='meal-sodium', blank=True, null=True)
    meal_potassium = models.FloatField(db_column='meal-potassium', blank=True, null=True)
    meal_rate = models.IntegerField(db_column='meal-rate', blank=True, null=True)
    meal_description = models.TextField(db_column='meal-description', blank=True, null=True)
    user = models.ForeignKey('users', models.DO_NOTHING, db_column='users_user-id')  # user_id
    categ_id = models.ForeignKey('FoodCategroies', models.DO_NOTHING, db_column='categ-id', null=True)  # categ_id

    class Meta:
        # managed = False
        db_table = 'meals'


class ProhibitedMeals(models.Model):
    meal_id = models.IntegerField(db_column='meal-id', primary_key=True)
    disease_id = models.IntegerField(db_column='disease-id', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'prohibited_meals'


