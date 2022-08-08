from django.http import HttpResponse
from django.shortcuts import render
from django.forms import formset_factory
from .models import Dish
from .forms import MenuForm


def home(request):
    return render(request, 'menu/home.html')


def menu_am(request):
    DishFormSet = formset_factory(form=MenuForm, extra=7)
    data = {
        'form-TOTAL_FORMS': '7',
        'form-INITIAL_FORMS': '0',
    }
    formset = DishFormSet(data)
    if request == "POST":
        formset = DishFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                return HttpResponse(form.cleaned_data())

    return render(request, 'menu/menu_am.html', {'formset': formset})


def menu_pm(request):
    menuform = MenuForm()
    context = {'menuform': menuform}
    return render(request, 'menu/menu_pm.html', context)
