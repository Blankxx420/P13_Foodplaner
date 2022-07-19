import json
from pprint import pprint

from django.core.management import BaseCommand
from menu.models import Dish
from menu.recipe_api import RecipeApi


def clear_db_dish():
    Dish.objects.all().delete()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        clear_db_dish()
        try:
            api = RecipeApi()
            api_data = api.get_recipe_from_dish_name()
            for details in api_data:
                Dish(
                    dish_name=details['title'],
                    recipe=details['instructions'],
                    ingredients=details['ingredients'],
                    serving=details['servings']
                ).save()
                self.stderr.write(self.style.SUCCESS("le plat " + details['title'] + " à bien été ajouté" ))
        except ValueError:
            self.stderr.write(self.style.ERROR('Une erreur est survenu.\n'
                                               'Il se peut que les aliments existe déjà.'))
