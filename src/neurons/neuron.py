from abc import ABC, abstractmethod

class Neuron(ABC):
    @abstractmethod
    def doTrain() -> None:
        pass
    
    @abstractmethod
    def predict() -> int:
        pass