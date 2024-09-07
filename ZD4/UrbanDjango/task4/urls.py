from .views import index, shop, cart
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import index, shop, cart

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
]