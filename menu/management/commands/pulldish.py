import json
from django.core.management import BaseCommand
from menu.models import Dish


def clear_db_dish():
    Dish.objects.all().delete()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        clear_db_dish()
        try:
            with open('menu/dish.json', 'r') as dish_file:
                dish_data = json.load(dish_file)
                for dish_name, recipe in dish_data['name'] and dish_data['recipe']:
                    if "'" in dish_name:
                        Dish(dish_name=dish_name.replace("'", " "), recipe=recipe).save()
                    else:
                        Dish(dish_name=dish_name, recipe=recipe).save()
                    self.stdout.write(f"{self.style.SUCCESS(dish_name)} ajouté à la base de données")
                self.stdout.write(self.style.SUCCESS('Les plats ont correctement été ajoutés dans la base de données'))
        except ValueError:
            self.stderr.write(self.style.ERROR('Une erreur est survenu.\nIl se peut que les aliments existe déjà.'))
