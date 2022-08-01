from django import forms
from .models import Dish


class MenuForm(forms.Form):

    dish = forms.ModelChoiceField(queryset=Dish.objects.all())
