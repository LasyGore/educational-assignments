from django.shortcuts import render

# Create your views here.

# task5/views.py
from django.shortcuts import render
from .forms import UserRegister


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']  # Псевдо-список существующих пользователей
    info = {'form': UserRegister()}  # Пустой словарь с формой

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            else:
                # Обрабатываем успешную регистрацию
                return render(request, 'fifth_task/success.html', {'username': username})

        info['form'] = form  # Передаем форму с ошибками

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    return sign_up_by_django(request)  # Просто перенаправляем запрос