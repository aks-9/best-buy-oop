from products import Product
from store import Store

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    # print(bose.buy(50))
    # print(mac.buy(100))
    # print(mac.is_active())
    #
    # bose.show()
    # mac.show()
    #
    # bose.set_quantity(1000)
    # bose.show()

    # instance of a store
    best_buy = Store([bose, mac])

    pixel = Product("Google Pixel 7", price=500, quantity=250)
    best_buy.add_product(pixel)
    best_buy.show_products()




if __name__ == "__main__":
    main()