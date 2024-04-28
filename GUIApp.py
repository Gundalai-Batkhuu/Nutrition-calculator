import tkinter as tk

def button_click():
    label.config(text="Calories calculated!")

root = tk.Tk()
root.title("Simple GUI")

# Create a label for the text "Choose a Recipe"
choose_label = tk.Label(root, text="Choose a Recipe")
choose_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)  # Place label in the first row, spanning both columns

label = tk.Label(root, text="Welcome to the Menu!")
label.grid(row=1, column=0, columnspan=2, padx=10, pady=10) # Add padding

# Create a Listbox widget
recipe_listbox = tk.Listbox(root)
recipe_listbox.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Add recipe names to the Listbox
recipes = ["Huushuur", "Buuz", "Pizza", "Lasagna", "Stir Fry"]  # Add your recipe names here
for recipe in recipes:
    recipe_listbox.insert(tk.END, recipe)

# Create a Scrollbar and associate it with the Listbox
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.grid(row=2, padx=(0,100), column=1, sticky="ns")

scrollbar.config(command=recipe_listbox.yview)

button = tk.Button(root, text="Calculate calories", bg="skyblue", command=button_click)
button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
