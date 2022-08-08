from django.http import HttpResponse
from django.shortcuts import render
from django.forms import formset_factory
from .models import Dish
from .forms import MenuForm


def home(request):
    return render(request, 'menu/home.html')


def menu_am(request):
    DishFormSet = formset_factory(form=MenuForm, extra=7)
    formset = DishFormSet()
    if request.method == "POST":
        formset2 = DishFormSet(request.POST)
        if formset2.is_valid():
            for form in formset2:
                if form.is_valid():
                    return HttpResponse(form.cleaned_data)
    return render(request, 'menu/menu_am.html', {'formset': formset})


def menu_pm(request):
    menuform = MenuForm()
    context = {'menuform': menuform}
    return render(request, 'menu/menu_pm.html', context)
