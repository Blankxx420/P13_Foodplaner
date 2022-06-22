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


class Dish(models.Model):
    dish_name = models.CharField(max_length=120, null=False, unique=True)
    recipe = models.TextField(null=False, unique=True)
    img_url = models.URLField(null=False, unique=True)

    def __str__(self):
        return self.dish_name


class Date(models.Model):
    day = models.DateField()
    time_days = models.CharField(max_length=120, null=False, unique=True)

    # pk ?
    def __str__(self):
        return self.day


class Menu(models.Model):
    menu_name = models.CharField(max_length=120, null=False, unique=True)
    notify_sms = models.BooleanField(default=False)

    # pk ?
