# Generated by Django 3.0.5 on 2022-12-12 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_auto_20221212_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='topping_name',
            field=models.CharField(max_length=200),
        ),
    ]