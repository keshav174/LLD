from Factories.whatsapp_template_factory import WhatsAppTemplateFactory
from Repositories.user_repository import UserRepository
from Services.notification_service_base import NotificationServiceBase


class WhatsAppNotificationService(NotificationServiceBase):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.template_factory = WhatsAppTemplateFactory()
        
    def send_notification(self, user_id: int, message: str, template_type: str = "recommendation"):
        user = self.user_repository.get_user_by_id(user_id)
        whatsapp_template = self.template_factory.get_template(template_type)
        whatsapp_content = whatsapp_template.generate_content(user, message)
        # Logic to send WhatsApp notification
        print(f"Sending WhatsApp notification to {user.phone_number} with content: {whatsapp_content}")