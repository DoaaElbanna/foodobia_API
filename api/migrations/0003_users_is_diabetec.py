# Generated by Django 2.1.7 on 2019-04-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_users_is_diabetes'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_diabetec',
            field=models.IntegerField(blank=True, db_column='is-diabetes', null=True),
        ),
    ]
