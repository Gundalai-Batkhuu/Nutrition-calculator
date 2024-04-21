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


if __name__ == "__main__":
    r = Recipe("Huushuur",
               [Ingredient("meat", 500), Ingredient("flour", 500), Ingredient("onion", 150), Ingredient("salt", 10)])
    l = Recipe("Buuz",
               [Ingredient("meat", 500), Ingredient("flour", 450), Ingredient("onion", 150), Ingredient("oil", 400),
                Ingredient("garlic", 60), Ingredient("salt", 10)])


    print("This recipe's name is: " + r.name)

    nutrition_reference = NutritionReference()

    calorie_value = r.calculate_calories(nutrition_reference)
    print("The calorie value is: " + str(calorie_value))

    widget_input = calorie_value
