from django.shortcuts import render

# Create your views here.
def func_platform(request):
    title = 'Главная страница'
    heading = 'Главная страница'
    href_1_text = 'Главная'
    href_2_text = 'Магазин'
    href_3_text = 'Корзина'
    context = {
        'title': title,
        'heading': heading,
        'href_1_text': href_1_text,
        'href_2_text': href_2_text,
        'href_3_text': href_3_text,
    }
    return render(request, 'third_task/platform.html',context)

def func_games(request):
    title = 'Магазин'
    heading = 'Игры'
    name_1_text = 'Atomic Heart'
    name_2_text = 'Cyberpunk 2077'
    name_3_text = 'PayDay 2'
    text_button_1 = 'Купить'
    text_button_2 = 'Вернуться обратно'
    context = {
        'title': title,
        'heading': heading,
        'name_1_text': name_1_text,
        'name_2_text': name_2_text,
        'name_3_text': name_3_text,
        'text_button_1': text_button_1,
        'text_button_2': text_button_2,
    }
    return render(request, 'third_task/games.html', context)

def func_cart(request):
    title = 'Корзина'
    heading = 'Извените, ваша корзина пуста'
    text_button_1 = 'Вернуться обратно'
    context = {
        'title': title,
        'heading': heading,
        'text_button_1': text_button_1,
    }
    return render(request, 'third_task/cart.html', context)