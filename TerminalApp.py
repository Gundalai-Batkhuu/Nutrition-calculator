from NutritionCalculator import NutritionCalculator


def display_menu():
    print("Welcome to the Nutrition Calculator!")
    print("1. Choose a recipe")
    print("2. Quit")


def get_user_choice():
    choice = input("Enter your choice: ")
    return choice


def invoke_option_1(recipes, nutrition_reference):
    print("Please select a recipe:")

    for i, recipe in enumerate(recipes):
        print(f"{i + 1}. {recipe.name}")

    recipe_choice = int(input("Enter the number of the recipe: "))
    print(f"You selected the recipe: {recipes[recipe_choice - 1].name}")

    print("The recipe contains the following ingredients:")
    recipe = recipes[recipe_choice - 1]
    for ingredient in recipe.ingredients:
        print(f"{ingredient.name}: {ingredient.quantity}g")

    print(f"The total calorie value of the recipe is {recipe.calculate_calories(nutrition_reference)}")

    print("Do you want to check another recipe?")
    answer = input("Enter 'y' to continue or any other key to exit: ")

    if answer.lower() == "y":
        return invoke_option_1(recipes, nutrition_reference)
    else:
        return "exit"


def main():
    calculator = NutritionCalculator('data/recipes.json', 'data/nutrition_values.csv')
    recipes = calculator.get_recipes()

    while True:
        display_menu()
        user_choice = get_user_choice()

        if user_choice == "1":
            continue_flag = invoke_option_1(recipes, calculator.nutrition_reference)
            if continue_flag == "exit":
                print("Exiting...")
                break

        elif user_choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

    print("Thank you for using the Nutrition Calculator!")


if __name__ == "__main__":
    main()
