from django.shortcuts import render
from task5.forms import ContactForm

# Create your views here.

def sign_up_by_html(request):
    users = ['Ivan', 'Petr', 'Vova',]
    info = {}

    if request.method == "POST":
        # Получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        info = {}

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'

        if username in users:
            info['error'] = 'Пользователь уже существует'

        if len(info) == 0:
            info['username'] = f'Приветствуем, {username}!'
    

    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_django(request): # предситавление формы через файл - forms.py
    users = ['Ivan', 'Petr', 'Vova', ]

    if request.method == "POST":
       # Получаем данные
       form = ContactForm(request.POST)
       info = {'form': form}
       if form.is_valid():
           # Обработка данных формы
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           repeat_password = form.cleaned_data['repeat_password']
           age = form.cleaned_data['age']
           # дальнейшая логика, например отправка email

           if password != repeat_password:
               info['error'] = 'Пароли не совпадают'

           if int(age) < 18:
               info['error'] = 'Вы должны быть старше 18'

           if username in users:
               info['error'] = 'Пользователь уже существует'

           if len(info) == 1:
               info['username'] = f'Приветствуем, {username}!'
    else:
        form = ContactForm()
        info = {'form': form}

    return render(request, 'fifth_task/registration_page_py.html', info)