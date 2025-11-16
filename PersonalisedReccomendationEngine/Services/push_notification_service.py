from Factories.push_notification_template_factory import PushNotificationTemplateFactory
from Repositories.user_repository import UserRepository
from Services.notification_service_base import NotificationServiceBase


class PushNotificationService(NotificationServiceBase):

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.template_factory = PushNotificationTemplateFactory()
    
    def send_notification(self, user_id: int, message: str, template_type: str = "recommendation"):
        user = self.user_repository.get_user_by_id(user_id)
        push_notification_template = self.template_factory.get_template(template_type)
        push_notification_content = push_notification_template.generate_content(user, message)
        # Logic to push notification
        print(f"Sending push notification to user {user_id}: {push_notification_content}")