# Generated by Django 4.0.4 on 2022-12-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.BooleanField(choices=[(True, 'Fragile'), (False, 'Non-Fragile')], null=True),
        ),
    ]