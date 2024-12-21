from django.shortcuts import render

# Главная страница
def main_page(request):
    return render(request, 'fourth_task/main_page.html')

# Страница магазина
def shop_page(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'Doom Eternal']
    return render(request, 'fourth_task/shop_page.html', {'games': games})

# Страница корзины
def cart_page(request):
    return render(request, 'fourth_task/cart_page.html')
