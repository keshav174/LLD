from Template.template_base import TemplateBase


class PushNotificationTemplate(TemplateBase):
    def __init__(self):
        super().__init__(header="Push Notification Header", footer="Push Notification Footer")

    def generate_content(self, user, message: str) -> str:
        return f"{self.header}\nHello {user.first_name},\n{message}\n{self.footer}"