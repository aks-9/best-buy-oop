class Product:
    """
        Represents a product in a store.

        Attributes:
            name (str): The product name.
            price (float): The product price.
            quantity (int): The current quantity in stock.
            active (bool): Whether the product is available.
        """

    def __init__(self, name, price, quantity):
        """
               Initialize a Product instance.

               Raises:
                   ValueError: If name is empty, or price/quantity is negative.
        """

        #validation
        if not name or not isinstance(name, str):
            raise ValueError('Product name must not be an empty string')
        if price < 0:
            raise ValueError('Product price can not be negative')
        if quantity < 0:
            raise ValueError('Product quantity can not be negative')

        #Instance variables
        self.name = name
        self.price = float(price)
        self. quantity = int(quantity)
        self.active = True



    def get_quantity(self):
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """
               Set the quantity of the product.

               Deactivates the product if quantity reaches 0.

               Raises:
                   ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError('Product quantity can not be negative!')
        self.quantity = int(quantity)

        if quantity == 0:
            self.active = False

    def is_active(self):
        """
                Return True if the product is active, otherwise False.
        """
        return self.active


    def activate(self):
        """
                Activate the product by setting its active status to True.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product by setting the active status to False.
        """
        self.active = False

    def show(self):
        """
        Prints a string that represents the product

        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """
            Buy a given quantity of the product.

            Args:
                quantity (int): The number of items to purchase.

            Returns:
                float: Total price of the purchase.

            Raises:
                ValueError: If quantity is negative or exceeds available stock.
                Exception: If the product is inactive.
        """
        if not self.active:
            raise Exception (f"Cannot buy '{self.name}': product is inactive.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if quantity > self.quantity:
            raise ValueError(
                f"Cannot buy {quantity} items: only {self.quantity} available."
            )

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return total_price


