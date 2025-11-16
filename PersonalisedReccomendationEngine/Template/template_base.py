
from abc import ABC, abstractmethod


class TemplateBase(ABC):
    def __init__(self, header: str = "", footer: str = ""):
        self.header = header
        self.footer = footer
    
    @abstractmethod
    def generate_content(self, user, message: str) -> str:
        pass