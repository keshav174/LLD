from Repositories.user_repository import UserRepository
from Repositories.cart_repository import CartRepository
from Repositories.order_repository import OrderRepository
from Entities.user import User
from Entities.cart import cart
from Entities.product import Product
from Entities.order import Order
from Services.email_notification_service import EmailNotificationService
from Services.push_notification_service import PushNotificationService
from Services.whatsapp_notification_service import WhatsAppNotificationService

class PersonalisedRecommendationSystemSingleton:
    _instance = None

    #Singleton  class 
    def __new__(cls):
            if cls._instance is None:
                cls._instance = super(PersonalisedRecommendationSystemSingleton, cls).__new__(cls)
            return cls._instance
    
    def __init__(self):
        self.user_repository = UserRepository()
        self.cart_repository = CartRepository()
        self.order_repository = OrderRepository()

    def initialize_system(self):
        #initialize with some users
        user1 = User(user_id=1, phone_number= "123", email="test1", address="test1", first_name="test1", last_name="test1")
        user2 = User(user_id=2, phone_number= "456", email="test2", address="test2", first_name="test2", last_name="test2")
        user3 = User(user_id=3, phone_number= "789", email="test3", address="test3", first_name="test3", last_name="test3")
        self.user_repository.add_user(user1)
        self.user_repository.add_user(user2)
        self.user_repository.add_user(user3)

        #initialize with some products
        product1 = Product(product_id=1, name="Product1", price=10.0)
        product2 = Product(product_id=2, name="Product2", price=20.0)
        product3 = Product(product_id=3, name="Product3", price=30.0)

        #initialize with some carts
        cart1 = cart(cart_id=1, user_id=1, Products=[product1, product2], total_price=30.0)
        cart2 = cart(cart_id=2, user_id=2, Products=[product2, product3], total_price=50.0)
        self.cart_repository.add_cart(cart1)
        self.cart_repository.add_cart(cart2)

        #initialize with some orders
        order1 = Order(order_id=1, user_id=1, price=30.0, status="delivered", Products=[product1, product2], date="2024-01-01")
        order2 = Order(order_id=2, user_id=2, price=50.0, status="shipped", Products=[product2, product3], date="2024-02-01")
        self.order_repository.add_order(order1)
        self.order_repository.add_order(order2)
    
    def send_email(self, user_id: int, message: str, template_type: str = "recommendation"):
        email_service = EmailNotificationService(self.user_repository)
        email_service.send_notification(user_id, message, template_type)

    def send_push_notification(self, user_id: int, message: str, template_type: str = "recommendation"):
        push_service = PushNotificationService(self.user_repository)
        push_service.send_notification(user_id, message, template_type)

    def send_whatsapp_notification(self, user_id: int, message: str, template_type: str = "recommendation"):
        whatsapp_service = WhatsAppNotificationService(self.user_repository)
        whatsapp_service.send_notification(user_id, message, template_type)



if __name__ == "__main__":
    personalised_recommendation_system = PersonalisedRecommendationSystemSingleton()
    personalised_recommendation_system.initialize_system()
    personalised_recommendation_system.send_email(user_id=1, message="Check out our new products!", template_type="recommendation")
    print("-----------------------------------\n")
    personalised_recommendation_system.send_push_notification(user_id=2, message="Exclusive offer just for you!", template_type="recommendation")
    print("-----------------------------------\n")
    personalised_recommendation_system.send_whatsapp_notification(user_id=3, message="Don't miss our latest deals!", template_type="recommendation")
    print("-----------------------------------\n")