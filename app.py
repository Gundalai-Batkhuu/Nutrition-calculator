class Recipe:
    name: str
    ingredients: list

    def __init__(self, name: str, ingredients: list):
        self.name = name
        self.ingredients = ingredients

    def calculate_calories(self):
        """
        Sums all the calories of the recipe's ingredients
        :return:
        """
        sum = 0

        for ingredient in self.ingredients:
            sum = sum + ingredient.calorie

        return sum


class Ingredient:
    name: str
    calorie: int

    def __init__(self, name: str, calorie: int):
        self.name = name
        self.calorie = calorie


if __name__ == "__main__":
    jor = Recipe("Huushuur",
                 [Ingredient("Meat", 500), Ingredient("Flour", 120), Ingredient("Onion", 200), Ingredient("Salt", 10)])
    print("This recipe's name is: " + jor.name)

    print("These are the ingredients list: ")
    for ingredient in jor.ingredients:
        print(ingredient.name)
        print(ingredient.calorie)

    print(jor.calculate_calories())

