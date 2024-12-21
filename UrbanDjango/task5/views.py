from django.shortcuts import render
from .forms import UserRegister

# Псевдо-список существующих пользователей
existing_users = ['user1', 'user2', 'user3']


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in existing_users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                greeting = f'Приветствуем, {username}!'
                return render(request, 'fifth_task/registration_page.html', {'greeting': greeting})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', {'error': info.get('error'), 'form': form})


def sign_up_by_html(request):
    return sign_up_by_django(request)

