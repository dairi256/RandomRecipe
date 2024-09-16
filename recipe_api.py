import requests
import random

API_KEY = 'f0535df3c4fe46ea90194ce80bb6ebb4'
BASE_URL = 'https://api.spoonacular.com/recipies'

def get_random_recipe():
    url = f"{BASE_URL}/random?apiKey={API_KEY}"
    response = requests.get(url)

    # This checks if the request was successful.
    if response.status_code == 200:
        recipe = response.json()
        return recipe['recipies'][0] #This returns the first recipe from the response.
    else:
        print("Error fetching random recipe:", response.status_code)
        return None

def find_recipies_by_ingredients(ingredients):
    ingredients_str = ','.join(ingredients)
    url = f"{BASE_URL}/findByIngredients?apiKey={API_KEY}&ingredients={ingredients_str}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json() # Returns the list of matched recipies based on the users prompt. 
    else:
        print("Error fetching recipies by ingredients:", response.status_code)
        return None