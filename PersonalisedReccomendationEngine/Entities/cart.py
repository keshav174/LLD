from Entities.product import Product


class cart:

    def __init__(self, cart_id, user_id, Products, total_price = 0.0):
        self.cart_id = cart_id
        self.user_id = user_id
        self.Products = Products
        self.total_price = total_price