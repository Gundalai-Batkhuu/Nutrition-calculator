import json


class NutritionReference:
    nutrition_reference: dict

    def __init__(self, filename):
        import csv

        self.nutrition_reference = {}
        # Open the CSV file
        with open(filename, newline='') as csvfile:
            # Create a CSV reader object
            csv_reader = csv.DictReader(csvfile)

            # Iterate over each row in the CSV file
            for row in csv_reader:
                self.nutrition_reference[row['ingredient']] = int(row['calorie'])

    def get_calorie_value(self, name):
        return self.nutrition_reference[name]


class Recipe:
    name: str
    ingredients: list

    def __init__(self, name: str):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def calculate_calories(self, nutrition_reference: NutritionReference):
        sum = 0
        for ingredient in self.ingredients:
            calorie_value_this_ingredient = (ingredient.quantity / 100) * nutrition_reference.get_calorie_value(
                ingredient.name)
            sum = sum + calorie_value_this_ingredient
        return sum


class Ingredient:
    name: str
    quantity: int

    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity


class NutritionCalculator:
    recipes = []
    nutrition_reference : NutritionReference

    def __init__(self, recipe_file, nutrition_reference_file):
        self.nutrition_reference = NutritionReference(nutrition_reference_file)

        with open(recipe_file, 'r') as f:
            recipes_data = json.load(f)

        for recipe_data in recipes_data:
            recipe = Recipe(recipe_data['recipe_name'])

            for ingredient_data in recipe_data['ingredients']:
                ingredient = Ingredient(ingredient_data['name'], ingredient_data['quantity'])
                recipe.add_ingredient(ingredient)

            self.recipes.append(recipe)

    def get_recipes(self):
        return self.recipes

    def calculate_calories(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                return recipe.calculate_calories(self.nutrition_reference)
        return None