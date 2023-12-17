from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, description: str, console_ui):
        self._description = description
        self.console_ui = console_ui

    @property
    def description(self) -> str:
        return self._description

    @abstractmethod
    def execute(self):
        pass
