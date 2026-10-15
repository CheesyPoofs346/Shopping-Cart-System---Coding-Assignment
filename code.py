# import datetime for the receipt
import datetime

# store lists and cart lists
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]
shopping_cart = []
quantities = []


# shows the store items
def display_products(products_list, prices_list):
    print("\n========== AVAILABLE PRODUCTS ==========\n")
    for i in range(len(products_list)):
        print(f"{i + 1}. {products_list[i]:<12} ${prices_list[i]:.2f}")


# adds item or goes up by 1
def add_product(products_list, prices_list, cart, qty_list):
    display_products(products_list, prices_list)
    print()
    choice = int(input("Enter product number: "))

    # check if product number is valid
    while choice < 1 or choice > len(products_list):
        print("\nInvalid product!")
        print(f"Please choose a number between 1 and {len(products_list)}.")
        choice = int(input("Enter product number: "))

    selected_product = products_list[choice - 1]

    # check if item is already in the cart
    if selected_product in cart:
        cart_index = cart.index(selected_product)
        qty_list[cart_index] += 1
        print(f"\n{selected_product} quantity increased to {qty_list[cart_index]}!")
    else:
        cart.append(selected_product)
        qty_list.append(1)
        print(f"\n{selected_product} was added to your cart!")


# takes item out or lowers quantity
def remove_product(cart, qty_list):
    if len(cart) == 0:
        print("\nYour shopping cart is empty!")
        print("There is nothing to remove.")
    else:
        print("\n========== YOUR SHOPPING CART ==========\n")
        for i in range(len(cart)):
            print(f"{i + 1}. {cart[i]} - Quantity: {qty_list[i]}")

        print("\nWhich item would you like to remove?")
        choice = int(input("Enter item number: "))

        # check if item is in the cart
        while choice < 1 or choice > len(cart):
            print("\nThat item does not exist in your cart!")
            choice = int(input("Enter item number: "))

        remove_index = choice - 1
        item_name = cart[remove_index]

        # lower quantity or delete it from both lists
        if qty_list[remove_index] > 1:
            qty_list[remove_index] -= 1
            print(f"\nOne {item_name} was removed!")
            print(f"\n{item_name} quantity is now {qty_list[remove_index]}.")
        else:
            cart.pop(remove_index)
            qty_list.pop(remove_index)
            print(f"\n{item_name} was removed from your cart!")


# gets the total price with quantities
def calculate_total(cart, qty_list, products_list, prices_list):
    subtotal = 0.0
    for i in range(len(cart)):
        item_name = cart[i]
        item_qty = qty_list[i]
        price_index = products_list.index(item_name)
        item_price = prices_list[price_index]
        subtotal += item_price * item_qty
    return subtotal


# shows the cart table
def display_cart(cart, qty_list, products_list, prices_list):
    if len(cart) == 0:
        print("\nYour shopping cart is empty!")
    else:
        print("\n========== YOUR SHOPPING CART ==========\n")
        print("Product         Price     Quantity     Total\n")
        total_items = 0
        for i in range(len(cart)):
            name = cart[i]
            qty = qty_list[i]
            price = prices_list[products_list.index(name)]
            product_total = price * qty
            total_items += qty
            print(f"{i + 1}. {name:<12} ${price:<8.2f} {qty:<12} ${product_total:.2f}")

        subtotal = calculate_total(cart, qty_list, products_list, prices_list)
        print(f"\nTotal Items: {total_items}")
        print(f"\nSubtotal: ${subtotal:.2f}")


# checks what discount they get
def calculate_discount(subtotal):
    if subtotal >= 40:
        return 15
    elif subtotal >= 20:
        return 10
    elif subtotal >= 10:
        return 5
    else:
        return 0


# main menu loop
running = True
while running:
    print("\n========== SMART SHOPPING CART ==========\n")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout\n")

    menu_choice = int(input("Enter your choice: "))

    # make sure choice is 1 to 6
    while menu_choice < 1 or menu_choice > 6:
        print("\nInvalid option!")
        menu_choice = int(input("Enter your choice: "))

    # do the menu options
    if menu_choice == 1:
        display_products(products, prices)

    elif menu_choice == 2:
        add_product(products, prices, shopping_cart, quantities)

    elif menu_choice == 3:
        remove_product(shopping_cart, quantities)

    elif menu_choice == 4:
        display_cart(shopping_cart, quantities, products, prices)

    elif menu_choice == 5:
        print("\n========== CURRENT TOTAL ==========\n")
        if len(shopping_cart) == 0:
            print("Your shopping cart is empty!\n")
            print("Subtotal: $0.00")
        else:
            for i in range(len(shopping_cart)):
                name = shopping_cart[i]
                qty = quantities[i]
                price = prices[products.index(name)]
                item_total = price * qty
                print(f"{name}: {qty} x ${price:.2f} = ${item_total:.2f}")
            sub = calculate_total(shopping_cart, quantities, products, prices)
            print(f"\nSubtotal: ${sub:.2f}")

    # checkout and print the receipt
    elif menu_choice == 6:
        if len(shopping_cart) == 0:
            print("\nYour shopping cart is empty! Please add items before checking out.")
        else:
            today_date = datetime.date.today().strftime("%m/%d/%Y")
            subtotal = calculate_total(shopping_cart, quantities, products, prices)
            discount_pct = calculate_discount(subtotal)
            saved = subtotal * (discount_pct / 100)
            final_total = subtotal - saved

            print("\n========== RECEIPT ==========\n")
            print(f"Date: {today_date}\n")
            for i in range(len(shopping_cart)):
                name = shopping_cart[i]
                qty = quantities[i]
                price = prices[products.index(name)]
                print(f"{name:<12} x{qty:<4} ${price * qty:.2f}")

            print(f"\nSubtotal:       ${subtotal:.2f}")
            print(f"Discount:       {discount_pct}%")
            print(f"Amount Saved:   ${saved:.2f}\n")
            print(f"Final Total:    ${final_total:.2f}\n")
            print("Thank you for shopping!")
            running = False