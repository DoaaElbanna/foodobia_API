# Generated by Django 2.1.7 on 2019-06-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190628_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_image',
            field=models.ImageField(blank=True, db_column='user-image', null=True, upload_to=''),
        ),
    ]