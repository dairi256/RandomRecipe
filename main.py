from recipe_api import get_random_recipe, find_recipies_by_ingredients

def main():
    # Test getting a random recipe
    print("Fetching a random recipe...\n")
    random_recipe = get_random_recipe()
    if random_recipe:
        print(f"Recipe: {random_recipe['title']}")
        print(f"Instructions: {random_recipe['instructions']}")
        print(f"Link: {random_recipe['sourceUrl']}")

    # Test finding recipies by ingredients. 
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    ingredients = [ingredient.strip() for ingredient in ingredients] # Cleaning up whitespaces.
    print("\nFetching recipies that include your ingredients...\n")
    recipies = find_recipies_by_ingredients(ingredients)
    if recipies:
        for recipe in recipies:
            print(f"Recipe:{recipe['title']}")
            print(f"Link: {recipe['sourceUrl']}")
    else:
        print("No recipies found matching those ingredients.")
if __name__ == '__main__':
    main()