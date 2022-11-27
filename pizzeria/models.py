from django.db import models
from django.core.validators import MinValueValidator


class Topping(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/toppings')

    def __str__(self):
        return f"{self.name}"


class PizzaBaseModel(models.Model):
    toppings = models.ManyToManyField(Topping)


class PizzaMenu(PizzaBaseModel):
    """This is a pizza from the menu, it has a customized image and a fixed price"""
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/pizzas')
    price = models.IntegerField(default=8, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name}"


class PizzaCustom(PizzaBaseModel):
    """This is a custom pizza created by the user, the price will be defined by the amount of toppings"""
    # customer = models.ForeignKey(User)
    price = models.IntegerField()

    def save(self, *args, **kwargs):
        self.price = len(self.toppings.all())


class ShoppingCart(models.Model):
    pizzas = models.ManyToManyField(PizzaBaseModel)
