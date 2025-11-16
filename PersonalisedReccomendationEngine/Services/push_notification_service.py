from Factories.push_notification_template_factory import PushNotificationTemplateFactory
from Repositories.user_repository import UserRepository
from Services.notification_service_base import NotificationServiceBase


class PushNotificationService(NotificationServiceBase):
    def send_notification(self, user_id: int, message: str):
        user = UserRepository.get_user_by_id(self, user_id)
        push_notification_temaplate = PushNotificationTemplateFactory.get_template("recommendation")
        push_notification_content = push_notification_temaplate.generate_content(user, message)
        # Logic to push notification
        print(f"Sending push notification to user {user_id}: {push_notification_content}")