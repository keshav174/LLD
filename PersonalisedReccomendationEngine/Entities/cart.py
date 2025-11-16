class cart:
    cart_id: int
    user_id: int
    Products: list
    total_price : float = 0
    
    def __init__(self, cart_id, user_id, Products, total_price):
        self.cart_id = cart_id
        self.user_id = user_id
        self.Products = Products
        self.total_price = total_price