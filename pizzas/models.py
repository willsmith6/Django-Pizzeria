from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ing',blank=True,null=True)


    def __str__(self):
        return self.pizza_name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizza_name = models.TextField()
    topping_name = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.pizza_name[:50]}...."

class MyModel(models.Model):
    upload = models.ImageField(upload_to='uploads')