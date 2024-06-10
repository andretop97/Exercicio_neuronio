import random
from src.utils.linear_algebra import *
from src.neurons.neuron import Neuron
from src.activation_functions.activation_function import ActivationFunction
from src.activation_functions.bipolar_step import BipolarStep


class Perceptron(Neuron):
    def _varible_initializer(self, train_inputs: list[list[float]]) -> None:
        self._set_initial_shape(train_inputs)
        self._set_initial_weights()
        self._set_initial_bias()

    def _set_initial_bias(self) -> None:
        self.bias = random.random()

    def _set_initial_weights(self) -> None:
        self.weights = [random.random() for i in range(self.shape[1])]

    def _set_initial_shape(self, train_inputs: list[list[float]]) -> None:
        self.shape = (len(train_inputs), len(train_inputs[0]))

    def _recalculateWeights(self, train_input: list[float], decision_erro: list[float], learning_rate: float) -> None:
        self.weights = soma_vetorial(self.weights, multiplicacao_escalar(train_input, decision_erro * learning_rate))

    def _calculateInference(self, train_input) -> float:
        signal = 0
        for i in range(self.shape[1]):
            signal += self.weights[i] * train_input[i]
        signal += self.bias 
        return signal
    
    def doTrain(
            self, 
            train_inputs: list[list[float]], 
            train_inputs_validation: list[float], 
            max_iterations: int = 100, 
            threshold: float = 0, 
            learning_rate: float = 0.01,
            activate_function: ActivationFunction = BipolarStep()
            ) -> tuple[float, float]:
        
        self._varible_initializer(train_inputs)

        epoch = 1
        loss = threshold -1 
        while epoch < max_iterations and loss < threshold:
            decision_erro_list: list[float] = []
            for i in range(self.shape[0]):
                pre_activation_value = self._calculateInference(train_inputs[i])
                decision_value = activate_function.calculate(pre_activation_value)
                decision_erro_list.append(train_inputs_validation[i] - decision_value)
                self._recalculateWeights(train_inputs[i], decision_erro_list[i], learning_rate)
                self.bias = self.bias + (learning_rate * decision_erro_list[i])
            loss = sum(decision_erro_list)
            print(decision_erro_list, epoch)
            epoch = epoch + 1
        return self.weights, self.bias


    def predict() -> int:
        pass

