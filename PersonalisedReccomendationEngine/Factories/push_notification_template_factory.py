from Factories.templatefactory_base import TemplateFactoryBase
from Template.push_notification_template import PushNotificationTemplate


class PushNotificationTemplateFactory(TemplateFactoryBase):

    def get_template(self, template_type: str):
        if template_type == "recommendation":
            return PushNotificationTemplate()
        elif template_type == "promotion":
            return PushNotificationTemplate()
        else:
            raise ValueError(f"Unknown template type: {template_type}")