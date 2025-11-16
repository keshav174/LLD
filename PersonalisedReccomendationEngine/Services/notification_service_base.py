from abc import ABC, abstractmethod
from  Repositories.user_repository import UserRepository
class NotificationServiceBase(ABC):

    @abstractmethod
    def send_notification(self, user_id: int, message: str):
        pass

