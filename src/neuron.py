from abc import ABC, abstractmethod

class Neuron(ABC):
    ...
    def __init__(self, train_inputs: list[list[float]], train_inputs_validations: list[int], epochs: int = 100) -> None:
        super().__init__()
        self.epochs: int = epochs
        self.train_inputs: list[list[float]] = train_inputs
        self.train_inputs_validations: list[int] = train_inputs_validations

        # Epsilon=.0000001, alpha=.1

        self.weights: list[int]
        self.bias: list[int]
        self.shape: tuple[str, int] = {'x': 0 , 'y': 0}


    @abstractmethod
    def doTrain() -> None:
        pass
    
    @abstractmethod
    def predict() -> int:
        pass