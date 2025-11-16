from Factories.whatsapp_template_factory import WhatsAppTemplateFactory
from Repositories.user_repository import UserRepository
from Services.notification_service_base import NotificationServiceBase


class WhatsAppNotificationService(NotificationServiceBase):
    
    def send_notification(self, user_id: int, message: str):
        user = UserRepository.get_user_by_id(self, user_id)
        whatsapp_template = WhatsAppTemplateFactory.get_template("recommendation")
        whatsapp_content = whatsapp_template.generate_content(user, message)
        # Logic to send WhatsApp notification
        print(f"Sending WhatsApp notification to {user.phone_number} with content: {whatsapp_content}")