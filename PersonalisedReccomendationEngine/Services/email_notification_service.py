from Factories.email_template_factory import EmailTemplateFactory
from Factories.push_notification_template_factory import PushNotificationTemplateFactory
from Repositories.user_repository import UserRepository
from Services.notification_service_base import NotificationServiceBase

class EmailNotificationService(NotificationServiceBase):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.template_factory = EmailTemplateFactory()

    def send_notification(self, user_id: int, message: str, template_type: str = "recommendation"):
        user = self.user_repository.get_user_by_id(user_id)
        email_template = self.template_factory.get_template(template_type)
        email_content = email_template.generate_content(user, message)
        # sending email
        print(f"Sending email to {user.email} with content: {email_content}")