# Generated by Django 3.0.5 on 2022-12-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='pizza_name',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topping',
            name='topping_name',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
