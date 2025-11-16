from abc import ABC, abstractmethod
from Template.template_base import TemplateBase


class TemplateFactoryBase(ABC):
    @abstractmethod
    def get_template(self, template_type: str) -> TemplateBase:
        pass