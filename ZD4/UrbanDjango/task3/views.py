from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = {
        'Игровая приставка': 'Купить',
        'Игра 1': 'Купить',
        'Игра 2': 'Купить',
    }
    return render(request, 'third_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')