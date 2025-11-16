from Factories.email_template_factory import EmailTemplateFactory
from Factories.push_notification_template_factory import PushNotificationTemplateFactory
from Repositories.user_repository import UserRepository
from Services.notification_service_base import NotificationServiceBase

class EmailNotificationService(NotificationServiceBase):

    def send_notification(self, user_id: int, message: str):
        user = UserRepository.get_user_by_id(self, user_id)
        email_template = EmailTemplateFactory.get_template("recommendation")
        email_content = email_template.generate_content(user, message)
        # sending email
        print(f"Sending email to {user.email} with content: {email_content}")