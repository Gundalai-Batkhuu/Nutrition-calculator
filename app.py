## Author: Nomuunaa Ganzorig
## Date created: 15 Apr 2024
## Date last changed: 26 Apr 2024
## This program calculates the nutrition of a meal.
## Input: reads / writes Output:


class NutritionReference:
    nutrition_reference: dict

    def __init__(self):
        filename = "calorie_values.csv"
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

    def __init__(self, name: str, ingredients: list):
        self.name = name
        self.ingredients = ingredients

    def calculate_weight(self):
        """
        Sums all the weight of the recipe's ingredients
        :return:
        """
        sum = 0
        for ingredient in self.ingredients:
            sum = sum + ingredient.weight

        return sum

    def calculate_calories(self, nutrition_reference: NutritionReference):

        sum = 0

        for ingredient in self.ingredients:
            calorie_value_this_ingredient = (ingredient.weight / 100) * nutrition_reference.get_calorie_value(
                ingredient.name)
            sum = sum + calorie_value_this_ingredient

        return sum


class Ingredient:
    name: str
    weight: int

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight




def print_menu():
    print("Welcome to the Menu!")
    print("1. Choose a Recipe")
    print("2. Display Recipe Ingredients")
    print("3. Calculate calories for a recipe")
    print("4. Exit")



if __name__ == "__main__":
    r = Recipe("Huushuur",
               [Ingredient("meat", 500), Ingredient("flour", 500), Ingredient("onion", 150), Ingredient("salt", 10)])
    l = Recipe("Buuz",
               [Ingredient("meat", 500), Ingredient("flour", 450), Ingredient("onion", 150), Ingredient("oil", 400),
                Ingredient("garlic", 30), Ingredient("salt", 10)])
    p = Recipe("Pizza",
                [Ingredient("flour", 300), Ingredient("tomato sauce", 200), Ingredient("cheese", 250), Ingredient("pepperoni", 150),
                 Ingredient("bell pepper", 100), Ingredient("onion", 100), Ingredient("olive oil", 50), Ingredient("salt", 10)])
    la = Recipe("Lasagna",
                [Ingredient("lasagna noodles", 400), Ingredient("meat", 500), Ingredient("tomato sauce", 150), Ingredient("ricotta cheese", 250), Ingredient("mozzarella cheese", 200),])
    s = Recipe("Stir Fry",
                [Ingredient("rice", 300), Ingredient("meat", 400), Ingredient("bell pepper", 150), Ingredient("carrot", 100), Ingredient("soy sauce", 100), Ingredient("garlic", 50), Ingredient("broccoli", 50), Ingredient("oil", 50), Ingredient("salt", 10)])

    print_menu()

    print("This recipe's name is: " + r.name)

    nutrition_reference = NutritionReference()

    calorie_value = r.calculate_calories(nutrition_reference)
    print("The calorie value is: " + str(calorie_value))

    widget_input = calorie_value

