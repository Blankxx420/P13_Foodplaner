""" models of app menu
Product:
- name -> varchar
- recipe -> text
Date:
- day -> varchar
Menu
- name -> varchar
- notifsms -> boolean
- pk one-to-many(date)
-pk one-to-many(product)

"""

from django.db import models
from users.models import User


class Dish(models.Model):
    dish_name = models.CharField(max_length=120, null=False, unique=True)
    recipe = models.TextField(null=False, unique=True)
    ingredients = models.TextField(null=True, unique=True)
    serving = models.CharField(max_length=120, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.dish_name


class Date(models.Model):
    day = models.CharField(max_length=120, null=False, unique=True)
    time_days = models.CharField(max_length=120, null=False, unique=False)
    objects = models.Manager()

    def __str__(self):
        return self.day


class Menu(models.Model):
    menu_name = models.CharField(max_length=120, null=False, unique=True)
    user_menu = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_date = models.ManyToManyField(Date)
    menu_dish = models.ManyToManyField(Dish)
    objects = models.Manager()

    def __str__(self):
        return self.menu_name


