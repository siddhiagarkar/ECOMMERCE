# Generated by Django 4.0.4 on 2023-06-16 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_user_customer_userr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='userr',
            new_name='user',
        ),
    ]
