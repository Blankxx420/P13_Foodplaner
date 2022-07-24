import json

import requests


class RecipeApi:

    def __init__(self):
        self.headers = {
            "X-RapidAPI-Key": "9166955388mshb38ea575d8c7514p1fccf0jsnc146294343f9",
            "X-RapidAPI-Host": "recipe-by-api-ninjas.p.rapidapi.com"
        }
        self.url = "https://recipe-by-api-ninjas.p.rapidapi.com/v1/recipe"

    def get_recipe_from_dish_name(self):
        dish_list = []
        with open("menu/dish.json", 'r') as dish_file:
            dish_data = json.load(dish_file)
            for dish_name in dish_data['name']:
                querystring = {'query': dish_name,
                               'offset': 0}
                response = requests.request("GET", self.url, headers=self.headers, params=querystring)
                response_data = response.json()
                for dict_data in response_data:
                    dish_list.append(dict_data)
            return dish_list

