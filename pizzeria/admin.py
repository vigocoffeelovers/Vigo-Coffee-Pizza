from django.contrib import admin

from pizzeria.models import PizzaMenu, Topping, ShoppingCart, PizzaCustom, PizzaBaseModel

admin.site.register(PizzaMenu)
admin.site.register(Topping)
admin.site.register(ShoppingCart)
admin.site.register(PizzaCustom)
admin.site.register(PizzaBaseModel)
