import unittest
from NutritionCalculator import NutritionCalculator


class MyTestCase(unittest.TestCase):
    recipe_file = '../data/recipes.json'
    nutrition_reference_file = '../data/nutrition_values.csv'
    calculator = NutritionCalculator(recipe_file, nutrition_reference_file)
    recipe = calculator.get_recipes()[0]
    print(recipe.name)

    def test_calorie_calculation(self):
        calorie_value = self.calculator.calculate_calories("Huushuur")
        self.assertEqual(3604.4, calorie_value)

        calorie_value = self.calculator.calculate_calories("Buuz")
        self.assertEqual(3255.0, calorie_value)


if __name__ == '__main__':
    unittest.main()
