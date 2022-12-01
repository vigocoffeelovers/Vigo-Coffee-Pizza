from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Topping(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/toppings', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Pizza(models.Model):
    """This is a pizza from the menu, it has a customized image and a fixed price"""
    toppings = models.ManyToManyField(Topping)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/pizzas')
    price = models.IntegerField(default=8, validators=[MinValueValidator(0)])
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class ShoppingCart(models.Model):
    pizzas = models.ManyToManyField(Pizza)


# class AppUser(User):
#     money = models.FloatField()
#     cart = ShoppingCart()
