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





