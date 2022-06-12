from django.db import models


class Meal(models.Model):
    """ Represent the database table meal"""
    id = models.BigAutoField()
    name = models.CharField(max_length=150, unique=True)
    recipe = models.TextField(unique=True)


class Menu(models.Model):
    """ Represent the dabatabe table menu"""
    day = models.CharField(max_length=150, unique=True)
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return self.day
