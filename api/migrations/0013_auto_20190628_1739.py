# Generated by Django 2.1.7 on 2019-06-28 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20190626_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meals',
            old_name='user',
            new_name='user_id',
        ),
    ]