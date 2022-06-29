import json
from django.core.management import BaseCommand
from menu.models import Dish


def clear_db_dish():
    Dish.objects.all().delete()


class Command(BaseCommand):

    def handle(self):
        clear_db_dish()
        try:
            with open('menu/dish.json', 'r') as dish_file:
                dish_data = json.load(dish_file)
                for dish_name in dish_data['name']:
                    if "'" in dish_name:
                        Dish(name=dish_name.replace("'", " ")).save()
                    else:
                        Dish(name=dish_name).save()
                    self.stdout.write(f"{self.style.SUCCESS(dish_name)} ajouté à la base de données")
                self.stdout.write(self.style.SUCCESS('Les plats ont correctement été ajoutés dans la base de données'))
        except ValueError:
            self.stderr.write(self.style.ERROR('Une erreur est survenu.\nIl se peut que les aliments existe déjà.'))
