from django.shortcuts import render
from .models import Dish


def home(request):
    return render(request, 'menu/home.html')


def menu_am(request):
    dish_obj = Dish.objects.all()
    context = {'dish_obj': dish_obj}
    return render(request, 'menu/menu_am.html', context)


def menu_pm(request):
    return render(request, 'menu/menu_pm.html')
