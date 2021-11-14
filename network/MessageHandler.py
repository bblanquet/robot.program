from abc import ABC, abstractmethod


class MessageHandler(ABC):
    @abstractmethod
    def handle(self, message: str):
        pass
