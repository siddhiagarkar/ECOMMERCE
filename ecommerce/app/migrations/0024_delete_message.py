# Generated by Django 4.2.2 on 2023-06-28 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_rename_name_customer_f_name_customer_l_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
