from Factories.templatefactory_base import TemplateFactoryBase
from Template.whatsapp_template import WhatsAppTemplate


class WhatsAppTemplateFactory(TemplateFactoryBase):
    def get_template(self, template_type: str):
        if template_type == "recommendation":
            return WhatsAppTemplate()
        elif template_type == "promotion":
            return WhatsAppTemplate()
        else:
            raise ValueError(f"Unknown template type: {template_type}")