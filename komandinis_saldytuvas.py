fridge = {}
recipe = {}
shopping_list = {}

while True:
    print("1. Add item to fridge")
    print("2. View items in fridge")
    print("3. Remove item from fridge")
    print("4. Add recipe and portions")
    print("5. View recipe and portions")
    print("6. Remove recipe")
    print("7. View shopping list")
    print("8. Quit")

    choice = input("Enter choice (1-8): ")

    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        if item in fridge:
            fridge[item] += quantity
        else:
            fridge[item] = quantity
        print(f"{quantity} {item}(s) added to fridge.\n")
    elif choice == "2":
        if not fridge:
            print("Fridge is empty.\n")
        else:
            print("Items in fridge:")
            for item, quantity in fridge.items():
                print(f"{item}: {quantity}")
            print()
    elif choice == "3":
        if not fridge:
            print("Fridge is empty.\n")
        else:
            item = input("Enter item name: ")
            if item in fridge:
                quantity = int(input(f"Enter quantity (up to {fridge[item]}): "))
                if quantity > fridge[item]:
                    print(
                        f"Error: Cannot remove {quantity} {item}(s). Only {fridge[item]} available in fridge.\n"
                    )
                else:
                    fridge[item] -= quantity
                    if fridge[item] == 0:
                        del fridge[item]
                    print(f"{quantity} {item}(s) removed from fridge.\n")
            else:
                print(f"Error: {item} not found in fridge.\n")
    elif choice == "4":
        recipe_name = input("Enter recipe name: ")
        recipe_portions = int(input("Enter number of portions: "))
        recipe_ingredients = {}
        while True:
            item = input("Enter item name (or 'done' to finish): ")
            if item == "done":
                break
            quantity = int(input("Enter quantity: "))
            recipe_ingredients[item] = quantity
        recipe[recipe_name] = {
            "portions": recipe_portions,
            "ingredients": recipe_ingredients,
        }
        print(f"{recipe_name} recipe added.\n")
    elif choice == "5":
        if not recipe:
            print("No recipes added yet.\n")
        else:
            print("Recipes:")
            for recipe_name, recipe_data in recipe.items():
                print(f"{recipe_name} ({recipe_data['portions']} portions):")
                for item, quantity in recipe_data["ingredients"].items():
                    print(f"{item}: {quantity*recipe_data['portions']} needed")
                print()
    elif choice == "6":
        if not recipe:
            print("No recipes added yet.\n")
        else:
            recipe_name = input("Enter recipe name to remove: ")
            if recipe_name in recipe:
                del recipe[recipe_name]
                print(f"{recipe_name} recipe removed.\n")
            else:
                print(f"Error: {recipe_name} recipe not found.\n")
    elif choice == "7":
        if not shopping_list:
            print("Shopping list is empty.\n")
        else:
            print("Shopping list:")
            for item, quantity in shopping_list.items():
                print(f"{item}: {quantity}")
            print()
    elif choice == "8":
        print("Goodbye!")
        break
