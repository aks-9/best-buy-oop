from products import Product
from store import Store


def start(store: Store):
    """
    Start the store menu.
    """
    while True:
        print("\nStore Menu")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            products = store.get_all_products()
            if not products:
                print("No active products available.")
            else:
                for idx, product in enumerate(products, start=1):
                    print(f"{idx}. ", end="")
                    product.show()

        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"Total quantity of all products in store: {total_quantity}")

        elif choice == "3":
            products = store.get_all_products()
            if not products:
                print("No active products available to order.")
                continue

            print("\nAvailable products:")
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")

            shopping_list = []
            while True:
                selection = input("Enter product number to buy (or 'done' to finish): ")
                if selection.lower() == "done":
                    break
                if not selection.isdigit() or int(selection) < 1 or int(selection) > len(products):
                    print("Invalid product number. Try again.")
                    continue

                product_idx = int(selection) - 1
                product = products[product_idx]

                quantity_str = input(f"Enter quantity for {product.name}: ")
                if not quantity_str.isdigit() or int(quantity_str) <= 0:
                    print("Invalid quantity. Try again.")
                    continue

                quantity = int(quantity_str)
                shopping_list.append((product, quantity))

            if not shopping_list:
                print("No products selected for order.")
                continue

            try:
                total_price = store.order(shopping_list)
                print(f"Order successful! Total price: {total_price}")
            except Exception as e:
                print(f"Error during order: {e}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(product_list)

# Start the store menu
start(best_buy)
