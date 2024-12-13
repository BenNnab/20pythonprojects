menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []
total = 0

def display_menu():
    print("------------MENU------------")
    for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")
    print("---------------------------")

def take_order():
    while True:
        food = input("Enter your preferred menu item (q to quit): ").lower()
        if food == "q":
            break
        elif food in menu:
            cart.append(food)
            print(f"{food.capitalize()} added to your cart.")
        else:
            print("Item not on the menu. Please choose a valid item.")

def display_order():
    global total
    print("----------Your Order----------")
    for food in cart:
        price = menu[food]
        total += price
        print(f"{food.capitalize():10} (${price:.2f})")
    print()
    print(f"Total is: ${total:.2f}")

# Main Program
display_menu()
take_order()
display_order()
