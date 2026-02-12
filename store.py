from products import Product
from typing import List

class Store:
    """
    Holds all of the products, and will allow the user to make a purchase of multiple products as one.

    Attributes:
        products (List[Product]): List of products in the store
    """

    def __init__(self, products: List[Product] = None): # Not using products=[] as it's a mutable value and then all instances of the class would share the same value. Using 'None', immutable value.
        """
                Initialize a Store instance.

                Args:
                    products (List[Product], optional): Initial list of products. Defaults to empty list.
        """
        if products is None:
            products = [] #Inside the function, checking if it’s None, and create a new list for each instance:Now every Store instance gets its own list.

        self.products = products


    def add_product(self, product: Product):# product should be an instance of the Product class.
        """
               Add a product to the store.

               Args:
                   product (Product): The product to add.
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the store.")
        self.products.append(product)

    def show_products(self):
        """
        Print all the products in the store

        """
        print(f'Total products: {len(self.products)}')
        for index, product in enumerate(self.products, start = 1):
            print(f"{index}." , end="")
            product.show()

    def remove_product(self, product):
        """
        Removes a product from the store.
        Args:
                   product (Product): The product to remove.
        Raises:
        ValueError: If the product does not exist in the store.
        """
        if product not in self.products:
            raise ValueError('Product not found in the store')
        self.products.remove(product) #using remove method on a list


    def get_total_quantity(self) -> int:
        """
         Return the total quantity of all products in the store.

        """
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List["Product"]:
        """
        Returns all products in the store that are active.

        """
        active_products = []

        for product in self.products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list) -> float:
        """
        Buy multiple products and return the total price.
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
