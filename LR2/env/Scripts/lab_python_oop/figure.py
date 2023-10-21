from abc import ABC, abstractmethod

class figuresh(ABC):
    @abstractmethod
    def repr(self):
        pass

    @abstractmethod
    def square(self):
        pass