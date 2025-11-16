from abc import ABC, abstractmethod
from  Repositories.user_repository import UserRepository
class NotificationServiceBase(ABC):

    @abstractmethod
    def send_notification(self, user_id: int, message: str):
        user = UserRepository.get_user_by_id(self, user_id)
        email_template = EmailTemplateFactory.get_template("recommendation")
        email_content = email_template.generate_content(user, message)
        # sending email
        print(f"Sending notification to {user.email} with content: {email_content}")

