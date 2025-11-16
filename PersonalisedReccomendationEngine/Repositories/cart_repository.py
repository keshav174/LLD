from Entities.cart import cart

class CartRepository:
    
    def __init__(self):
        self.carts: list[cart]  = []

    def add_cart(self, cart: cart):
        self.carts.append(cart)
    
    def get_carts(self) -> list[cart]:
        return self.carts
    
    def get_carts_by_user_id(self, user_id: int) -> list[cart]:
        return [cart for cart in self.carts if cart.user_id == user_id]
    
    def delete_cart(self, cart_id:int):
        self.carts = [cart for cart in self.carts if cart.cart_id != cart_id]