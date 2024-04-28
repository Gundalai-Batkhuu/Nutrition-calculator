import tkinter as tk
from NutritionCalculator import NutritionCalculator
from tkinter import Frame


class NutritionApp:
    calculator: NutritionCalculator
    recipes: list
    result_labels = []

    def __init__(self, root, calculator: NutritionCalculator):
        # Initialize the GUI
        self.root = root
        self.root.geometry("800x500")
        self.root.title("Nutrition Calculator")
        self.root.configure(bg="beige")

        # Store the calculator and its data
        self.calculator = calculator
        self.recipes = calculator.recipes
        self.nutrition_reference = calculator.nutrition_reference

        # Create GUI elements
        self.label = tk.Label(root, text="Welcome to the Menu!", bg="skyblue")
        self.label.pack()

        self.recipe_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.recipe_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.scrollbar.config(command=self.recipe_listbox.yview)
        self.recipe_listbox.config(yscrollcommand=self.scrollbar.set)
        for recipe in self.recipes:
            self.recipe_listbox.insert(tk.END, recipe.name)

        self.button_calculate_calories = tk.Button(root, text="Calculate calories for selected recipe",
                                                   command=self.calculate_and_show)
        self.button_calculate_calories.pack()

        self.button_exit = tk.Button(root, text="Exit", command=root.quit)
        self.button_exit.pack()

    def calculate_and_show(self):
        # Clear previous values on the root in the result_labels list
        if self.result_labels is not None:
            for label in self.result_labels:
                label.destroy()

        selected_index = self.recipe_listbox.curselection()
        if selected_index:
            selected_recipe = self.recipes[selected_index[0]]

            # Show ingredients
            ingredients_label = tk.Label(self.root, text="The recipe contains the following ingredients:",
                                         bg="skyblue")
            ingredients_label.pack()
            self.result_labels.append(ingredients_label)

            for ingredient in selected_recipe.ingredients:
                ingredient_label = tk.Label(self.root, text=f"{ingredient.name}: {ingredient.quantity}g", bg="skyblue")
                ingredient_label.pack()
                self.result_labels.append(ingredient_label)

            # Calculate calories
            calorie_value = selected_recipe.calculate_calories(self.nutrition_reference)
            result_label = tk.Label(self.root,
                                    text=f"The calorie value for {selected_recipe.name} is: {calorie_value}",
                                    bg="skyblue")
            result_label.pack()
            self.result_labels.append(result_label)


def main():
    root = tk.Tk()
    calculator = NutritionCalculator('data/recipes.json', 'data/nutrition_values.csv')
    NutritionApp(root, calculator)
    root.mainloop()


if __name__ == "__main__":
    main()
