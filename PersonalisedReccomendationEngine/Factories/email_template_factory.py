from  Factories.templatefactory_base import TemplateFactoryBase
from Template.email_template import EmailTemplate
class EmailTemplateFactory(TemplateFactoryBase):

    def get_template(self, template_type: str):
        if template_type == "recommendation":
            return EmailTemplate()
        elif template_type == "promotion":
            return EmailTemplate() 
        else:
            raise ValueError(f"Unknown template type: {template_type}")