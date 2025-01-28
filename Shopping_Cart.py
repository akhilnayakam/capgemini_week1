def add_item(cart):
    while True:
        item_name = input("Enter the item name: ").strip()
        if item_name:
            break
        else:
            print("Item name cannot be empty.")
    
    while True:
        item_price = input(f"Enter the price for {item_name}: ")
        if item_price.replace('.', '', 1).isdigit():
            item_price = float(item_price)
            if item_price > 0:
                cart.append({"name": item_name, "price": item_price})
                print(f"{item_name} added to the cart for {item_price}.")
                break
            else:
                print("Price must be greater than 0.")
        else:
            print("Invalid price. Please enter a valid amount.")

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nItems in your cart:")
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['name']} - {item['price']:.2f}")
        print("-" * 30)

def calculate_total(cart):
    if not cart:
        print("Your cart is empty. Total price is 0.00.")
    else:
        total_price = sum(item['price'] for item in cart)
        print(f"Total price of items in the cart: {total_price:.2f}")

def shopping_cart():
    print("Welcome to the Shopping Cart Program!")
    cart = []
    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Calculate Total Price")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                add_item(cart)
            elif choice == 2:
                view_cart(cart)
            elif choice == 3:
                calculate_total(cart)
            elif choice == 4:
                print("Thank you for using the Shopping Cart Program!")
                break
            else:
                print("Invalid option. Please select a number between 1 and 4.")
        else:
            print("Invalid input. Please enter a number.")

shopping_cart()
