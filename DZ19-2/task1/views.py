from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import Buyer, Game
# Create your views here.
def index(request):
    return render(request, 'tsk1/index.html')


def shop(request):
    games = Game.objects.all()  # Получаем все записи из таблицы Game
    return render(request, 'tsk1/shop.html', {'games': games})


def cart(request):
    return render(request, 'tsk1/cart.html')

def sign_up_by_django(request):
    info = {'form': UserRegister()}  # Пустой словарь с формой

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверяем, существует ли покупатель с таким именем
            if Buyer.objects.filter(name=name).exists():
                info['error'] = 'Пользователь уже существует'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            else:
                # Создаем нового покупателя
                Buyer.objects.create(name=name, age=age, balance=0 )
                return redirect('home')  # Перенаправляем на главную страницу

        info['form'] = form  # Передаем форму с ошибками

    return render(request, 'tsk1/registration_page.html', info)


def sign_up_by_html(request):
    return sign_up_by_django(request)  # Просто перенаправляем запрос