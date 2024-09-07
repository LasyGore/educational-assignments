from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def index(request):
    return render(request, 'fourth_task/index.html')


def shop(request):
    games = ["Atomic Heart", "Cyberpunk 2077"]
    return render(request, 'fourth_task/shop.html', {'games': games})


def cart(request):
    return render(request, 'fourth_task/cart.html')