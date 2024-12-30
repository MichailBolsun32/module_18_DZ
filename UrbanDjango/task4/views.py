from django.shortcuts import render

# вспомогательная ф-ция для создания списка меню
# используем список т.к. Django не поддерживает dict.items(), для итерации словаря
def get_menu():
    return [
        ['/platform/', 'Главная'],
        ['/platform/games/', 'Магазин'],
        ['/platform/cart/', 'Корзина'],
    ]

# Create your views here.
def func_platform(request):
    menu = get_menu()

    text_pagename = 'Главная страница'
    text_title = 'Главная страница'

    context = {
        'menu': menu,
        'text_pagename': text_pagename,
        'text_title': text_title,
    }
    return render(request,'fourth_task/menu.html', context)

def func_games(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2', ]
    text_button_1 = 'Купить'
    text_button_2 = 'Вернуться обратно'
    text_pagename = 'Игры'
    text_title = 'Магазин'
    text_href = '/platform/'

    menu = get_menu()

    context = {
        'games': games,
        'text_button_1': text_button_1,
        'text_button_2': text_button_2,
        'text_pagename': text_pagename,
        'text_title': text_title,
        'text_href': text_href,
        'menu': menu,
    }
    return render(request, 'fourth_task/games.html', context)

def func_cart(request):
    text_button_1 = 'Вернуться обратно'
    text_pagename = 'Корзина'
    text_title = 'Корзина'
    text_content = 'Извените, ваша корзина пуста'
    text_href = '/platform/'

    menu = get_menu()

    context = {
        'text_button_1': text_button_1,
        'text_pagename': text_pagename,
        'text_title': text_title,
        'text_content': text_content,
        'text_href': text_href,
        'menu': menu,
    }
    return render(request, 'fourth_task/cart.html', context)