from abc import ABC, abstractmethod
class ActivationFunction(ABC):

    @abstractmethod
    def calculate(self) -> float:
        pass