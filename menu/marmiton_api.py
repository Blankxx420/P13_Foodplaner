from pprint import pprint

from marmiton import Marmiton, RecipeNotFound
import json


class MarmitonApi:

    def __init__(self):
        self.dish_file_path = "dish.json"
        self.get_recipe_by_name_of_dish()

    def get_recipe_by_name_of_dish(self):
        with open(self.dish_file_path, 'r') as dish_file:
            dish_data = json.load(dish_file)
            for dish_name in dish_data['name']:
                query_options = {
                    "aqt": dish_name,  # Query keywords - separated by a white space
                    "dt": "platprincipal",  # Plate type : "entree", "platprincipal", "accompagnement", "amusegueule",
                    # "sauce" (optional)
                    "exp": 2,  # Plate price : 1 -> Cheap, 2 -> Medium, 3 -> Kind of expensive (optional)
                    "dif": 2,  # Recipe difficulty : 1 -> Very easy, 2 -> Easy, 3 -> Medium, 4 -> Advanced (optional)
                    "veg": 0,  # Vegetarien only : 0 -> False, 1 -> True (optional)
                }
                query_result = Marmiton.search(query_options)
                recipes = query_result['props']['pageProps']['searchResults']['hits']
                if recipes['title'] == dish_name:
                    recipe = recipes[0]
                    pprint(recipe, indent=2)


MarmitonApi()
