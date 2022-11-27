from django.urls import path

from .views import menu_view, custom_pizza_view, cart_view

urlpatterns = [
    path('', menu_view),
    path('menu/', menu_view),
    path('custom_pizza/', custom_pizza_view),
    path('cart/', cart_view),
]