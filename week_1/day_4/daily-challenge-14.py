""" Coffee Shop Menu Manager
You were hired to help a small coffee shop manage their product menu using Python.

Write a program that:
1. Stores the coffee shop menu in memory
2. Lets the user:

Create a new item
Read (view) all items
Update an item’s price
Delete an item
Exit
Your program must be organized with functions.
Do not write all the logic in one giant while loop.
You should split behavior into reusable functions."""

menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    """Print all drinks and prices."""
    if not menu_dict:
        print("The menu is empty")
    else:
        for drink, price in menu_dict.items():
            print(f"{drink} - {price}₪")
    pass
    

def add_item(menu_dict):
    """Add a new drink to the menu."""
    drink_input = input("Enter new drink name: ")
    price_input = float(input("Enter price: "))
    if drink_input not in menu:
        menu[drink_input] = price_input
        print(f"{drink_input} added!")
    else:
        print("Item already exists!")
    pass


def update_price(menu_dict):
    """Change the price of an existing drink."""
    drink_update = (input("Which drink do you want to update? "))
    if drink_update in menu:
        price_update = float(input("Enter new price: "))
        menu[drink_update] = price_update
        print("Price updated!")
    else:
        print("Item not found.")
    pass


def delete_item(menu_dict):
    """Remove a drink from the menu."""
    drink_delete = input("Which drink do you want to delete? ")
    if drink_delete in menu:
        del menu[drink_delete]
        print("Item deleted.")
    else:
        print("Item not found.")
    pass


def show_options():
    """Print the available actions."""
    print("What would you like to do?")
    print("1. Show menu")
    print("2. Add item")
    print("3. Update price")
    print("4. Delete item")
    print("5. Exit")
    pass

def run_coffee_shop(menu):
    """Main loop of the program."""
    # TODO
    # while True:
    #   1. show_options()
    #   2. get user choice
    #   3. if 1 -> show_menu(menu)
    #      if 2 -> add_item(menu)
    #      if 3 -> update_price(menu)
    #      if 4 -> delete_item(menu)
    #      if 5 -> print("Goodbye!") and break
    #      else -> "Invalid choice, try again."

    while True:
         show_options()
         choose_str = input("> ")
         choose = int(choose_str)
         if choose == 1:
            show_menu(menu)
         elif choose == 2:
            add_item(menu)
         elif choose == 3:
            update_price(menu)
         elif choose == 4:
            delete_item(menu)
         elif choose == 5:
            print("Goodbye!")
            break
         else:
            print("Invalid choice, try again.")
    pass

# Start the program
run_coffee_shop(menu)