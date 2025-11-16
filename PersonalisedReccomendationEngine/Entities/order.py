from Entities.product import Product
from datetime import date


class Order:

    def __init__(self, order_id, user_id, price, status, Products, date =date.today().strftime("%Y-%m-%d")):
        self.order_id = order_id
        self.user_id = user_id
        self.price = price
        self.status = status
        self.Products = Products
        self.date = date
