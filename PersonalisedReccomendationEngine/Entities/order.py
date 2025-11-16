class Order:
    order_id: int
    user_id: int
    price : float = 0 
    status: str
    Products: list
    date : str = date.today().strftime("%Y-%m-%d")

    def __init__(self, order_id, user_id, price, status, Products, date):
        self.order_id = order_id
        self.user_id = user_id
        self.price = price
        self.status = status
        self.Products = Products
        self.date = date
