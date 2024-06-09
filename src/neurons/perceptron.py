import random
from src.utils.linear_algebra import *
from src.neurons.neuron import Neuron
from src.activation_functions.activation_function import ActivationFunction


class Perceptron(Neuron):
    def __init__(self) -> None:
        super().__init__()

    def varible_initializer(self) -> None:
        self.set_initial_shape()
        self.set_initial_weights()
        self.set_initial_bias()

    def set_initial_bias(self) -> None:
        self.bias = random.random()

    def set_initial_weights(self) -> None:
        self.weights = [random.random() for i in range(self.shape[0])]

    def set_initial_shape(self, train_inputs: list[list[float]]) -> None:
        self.shape = (len(train_inputs), len(train_inputs[0]))

    def recalculateWeights(self, train_input: list[float], decision_erro: list[float], learning_rate: float) -> None:
        self.weights = soma_vetorial(self.weights, multiplicacao_escalar(train_input, decision_erro * learning_rate))

    def calculateInference(self, w, Xi, b):
        u = 0
        for i in range(len(w)):
            u = u + w[i] * Xi[i]
        u = u + b 
        return u
    
    def doTrain(
            self, 
            train_inputs: list[list[float]], 
            train_inputs_validation: list[float], 
            max_iterations: int = 100, 
            threshold: float = 0, 
            learning_rate: float = 0.001,
            activate_function: ActivationFunction = None
            ) -> None:
        
        self.varible_initializer(train_inputs)

        epoch = 1
        while epoch < max_iterations and loss > threshold:
            decision_erro_list = []
            for i in range(self.shape[0]):
                pre_activation_value = self.calculateInference(self.weights, train_inputs[i], self.bias)
                decision_value = funcao_ativacao(pre_activation_value)
                decision_erro_list.append(train_inputs_validation[i] - decision_value)
                self.recalculateWeights(train_inputs[i], decision_erro_list[i], learning_rate)
                self.bias = self.bias + (learning_rate * decision_erro_list[i])
            loss = len(decision_erro_list)
            epoch = epoch + 1
        return self.weights, self.bias


    def predict() -> int:
        pass

