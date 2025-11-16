from Services.notification_service_base import NotificationServiceBase


class PushNotificationService(NotificationServiceBase):
    
    def send_notification(self, user_id: int, message: str):
        # Logic to send push notification
        print(f"Sending push notification to user {user_id}: {message}")