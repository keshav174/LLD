from Template.template_base import TemplateBase


class EmailTemplate(TemplateBase):
    def __init__(self):
        super().__init__(header="Email Header", footer="Email Footer")

    def generate_content(self, user, message: str) -> str:
        return f"{self.header}\nHello {user.first_name},\n{message}\n{self.footer}"