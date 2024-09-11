# tsk1/urls.py
from django.urls import path, include
from .views import sign_up_by_django, sign_up_by_html
from .views import index, shop, cart
from django.contrib import admin


urlpatterns = [
    path('', sign_up_by_django, name='sign_up'),
    path('index/', index, name='home'),  # Добавьте этот путь
    path('django_sign_up/', sign_up_by_html, name='django_sign_up'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
]
#path('', sign_up_by_django, name='sign_up'),

#path('', index, name='index'),