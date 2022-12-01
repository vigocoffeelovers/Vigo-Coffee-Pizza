from django.shortcuts import render
from pizzeria.models import Pizza


def menu_view(request):
    template_name = 'menu.html'
    return render(request, template_name, {
        "pizzas": Pizza.objects.all()
    })


def cart_view(request):
    template_name = 'cart.html'
    return render(request, template_name)


def custom_pizza_view(request):
    template_name = 'custom_pizza.html'
    return render(request, template_name)
