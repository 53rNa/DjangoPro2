from django.shortcuts import render

# Главная страница
def main_page(request):
    return render(request, 'third_task/main_page.html')

# Страница магазина
def shop_page(request):
    items = {
        "Товар 1": "100 руб.",
        "Товар 2": "200 руб.",
        "Товар 3": "300 руб."
    }
    return render(request, 'third_task/shop_page.html', {'items': items})

# Страница корзины
def cart_page(request):
    return render(request, 'third_task/cart_page.html')

