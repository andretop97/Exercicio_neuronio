from abc import ABC, abstractmethod
class ActivationFunction(ABC):

    @abstractmethod
    def calculate(self, signal: float) -> float:
        pass