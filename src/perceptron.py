import random
from src.utils.linear_algebra import *
from src.neuron import Neuron


class Perceptron(Neuron):
    def __init__(self) -> None:
        super().__init__()
        self.weights = [random.random() for i in range(len(X[0]))]

    def doTrain() -> None:
        pass

    def predict() -> int:
        pass

# def perceptron(max_it, E, alpha, X, d):
#         w = [random.random() for i in range(len(X[0]))]
#         b = random.random()

#         t = 1
#         while t < max_it and E > 0:
#             e = []
#             for i in range(len(X)):
#                 y = funcao_ativacao(reta(w, X[i], b))
#                 e.append(d[i] - y)
#                 w = soma_vetorial(w, multiplicacao_escalar(X[i], e[i]*alpha))
#                 b = b + (alpha * e[i])
#             E = len(e)
#             t = t + 1
#             print(w, b)
#         return w,b


batata = Perceptron()