from django.shortcuts import render
from django.forms import formset_factory
from .models import Dish
from .forms import MenuForm


def home(request):
    return render(request, 'menu/home.html')


def menu_am(request):
    DishFormSet = formset_factory(form=MenuForm, extra=6)
    if request.method == 'POST':
        formset = DishFormSet(request.POST)
        context = {"formset": formset}
        if formset.is_valid():
            for form in formset:
                form.save()
            return render(request, 'menu/menu_am.html', context)


def menu_pm(request):
    context = {'menuform': MenuForm}
    return render(request, 'menu/menu_pm.html', context)
