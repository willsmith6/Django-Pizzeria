# Generated by Django 3.0.5 on 2022-12-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_auto_20221212_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(upload_to='uploads')),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ing'),
        ),
    ]