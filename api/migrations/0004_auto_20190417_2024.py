# Generated by Django 2.1.7 on 2019-04-17 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_users_is_diabetec'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingrediants',
            old_name='ingrediants_id',
            new_name='ingrediant_id',
        ),
        migrations.RenameField(
            model_name='ingrediants',
            old_name='ingrediants_name',
            new_name='ingrediant_name',
        ),
        migrations.RemoveField(
            model_name='meals',
            name='dislike_counter',
        ),
        migrations.RemoveField(
            model_name='meals',
            name='like_counter',
        ),
        migrations.AddField(
            model_name='ingrediants',
            name='potassium',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meals',
            name='meal_carbs',
            field=models.FloatField(blank=True, db_column='meal-carbs', null=True),
        ),
        migrations.AddField(
            model_name='meals',
            name='meal_fats',
            field=models.FloatField(blank=True, db_column='meal-fats', null=True),
        ),
        migrations.AddField(
            model_name='meals',
            name='meal_potassium',
            field=models.FloatField(blank=True, db_column='meal-potassium', null=True),
        ),
        migrations.AddField(
            model_name='meals',
            name='meal_protein',
            field=models.FloatField(blank=True, db_column='meal-protein', null=True),
        ),
        migrations.AddField(
            model_name='meals',
            name='meal_rate',
            field=models.IntegerField(blank=True, db_column='meal-rate', null=True),
        ),
        migrations.AddField(
            model_name='meals',
            name='meal_sodium',
            field=models.FloatField(blank=True, db_column='meal-sodium', null=True),
        ),
        migrations.AddField(
            model_name='meals',
            name='meal_sugar',
            field=models.FloatField(blank=True, db_column='meal-sugar', null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='fav_category',
            field=models.TextField(blank=True, db_column='fav-category', null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='user_phone',
            field=models.IntegerField(blank=True, db_column='user-phone', null=True),
        ),
        migrations.AlterField(
            model_name='meals',
            name='users_user_id',
            field=models.ForeignKey(db_column='users_user-id', on_delete=django.db.models.deletion.DO_NOTHING, to='api.users'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_diabetec',
            field=models.IntegerField(blank=True, db_column='is-diabetec', null=True),
        ),
    ]