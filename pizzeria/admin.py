from django.contrib import admin

from pizzeria.models import Pizza, Topping, ShoppingCart

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(ShoppingCart)
