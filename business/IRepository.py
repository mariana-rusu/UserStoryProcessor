from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def put_item(self, name, body):
        pass

