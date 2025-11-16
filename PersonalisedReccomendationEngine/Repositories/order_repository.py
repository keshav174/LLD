from Entities.order import Order


class OrderRepository:
    orders : list[Order] = []

    def add_order(self, order: Order):
        self.orders.append(order)
    
    def get_orders(self) -> list[Order]:
        return self.orders
    
    def get_orders_by_user_id(self, user_id: int) -> list[Order]:
        return [order for order in self.orders if order.user_id == user_id]
    
    def delete_order(self, order_id:int):
        self.orders = [order for order in self.orders if order.order_id != order_id]