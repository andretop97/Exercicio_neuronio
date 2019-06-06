import numpy as np
import matplotlib.pyplot as plt
import random
import math
from sklearn.metrics import mean_squared_error


def plotar(w1,w2,bias,title):
    xvals = np.arange(-1, 3, 0.01)     
    newyvals = (((xvals * w2) * - 1) - bias) / w1
    plt.plot(xvals, newyvals, 'r-')    
    plt.title(title)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.axis([-1,2,-1,2])
    plt.plot([0,1,0],[0,0,1], 'b^')
    plt.plot([1],[1], 'go')
    plt.xticks([0,1])
    plt.yticks([0,1])
    plt.show()


def funcao_ativacao(u):
    return 1 if u>0 else -1


def funcao_tgH(u):
    return math.tanh(u)


def reta(w, Xi, b):
    u = 0
    for i in range(len(w)):
        u = u + w[i] * Xi[i]
    u = u + b 
    return u


def soma_escalar(vetor, const):
    novo_vet = vetor
    for i in range(len(vetor)):
        novo_vet[i] = vetor[i] + const
    return novo_vet


def soma_vetorial(Vetor1, Vetor2):
    vetor_resultante = [0]*len(Vetor1)
    for i in range(len(Vetor1)):
        vetor_resultante[i] = Vetor1[i] + Vetor2[i]
    return vetor_resultante


def subtracao_vetorial(Vetor1, Vetor2):
    vetor_resultante = [0] * len(Vetor1)
    for i in range(len(Vetor1)):
        vetor_resultante[i] = Vetor1[i] - Vetor2[i]
    return vetor_resultante


def mul_escalar(Vetor1, const):
    vetor_resultante = [0]*len(Vetor1)
    for i in range(len(Vetor1)):
        vetor_resultante[i] = Vetor1[i]*const
    return vetor_resultante


def mul_ele_vetor(Vetor1,Vetor2):
    vetor_resultante = [0]*len(Vetor1)
    for i in range(len(Vetor1)):
        vetor_resultante[i] = Vetor1[i] * Vetor2[i]
    return vetor_resultante


def conta_erro(erro):
    numero_erro = 0
    for i in erro:
            numero_erro = numero_erro + 1
    return  numero_erro


def erro_quadratico_medio(Erro):
    MSE = 0
    for i in Erro:
        MSE = MSE + i**2
    MSE = MSE/len(Erro)
    return MSE


def adaline(max_it, Epsilon, alpha, X, d):
    w = [random.random() for i in range(len(X[0]))]
    b = random.random()
    t = 1
    e = [0 for x in range(len(X))] # [1]*len(X)
    validacao = True
    while validacao:
        MSEi = erro_quadratico_medio(e)
        for i in range(len(X)):
            y = funcao_tgH(reta(w, X[i], b))
            e[i] = d[i] - y
            w = soma_vetorial(w, mul_escalar(X[i], e[i]*alpha))
            b = b + alpha * e[i]
        MSEf = erro_quadratico_medio(e)
        t = t + 1
        delta_MSE = abs(MSEf-MSEi)
        validacao = t < max_it and delta_MSE > Epsilon
    print(f'Iterações: {t}, Delta_MSE: {delta_MSE}')
    return w, b


def perceptron(max_it, E, alpha, X, d):
        w = [random.random() for i in range(len(X[0]))]
        b = random.random()

        t = 1
        while t < max_it and E > 0:
            e = []
            for i in range(len(X)):
                y = funcao_ativacao(reta(w, X[i], b))
                e.append(d[i] - y)
                w = soma_vetorial(w, mul_escalar(X[i], e[i]*alpha))
                b = b + (alpha * e[i])
            E = conta_erro(e)
            t = t + 1
            print(w, b)
        return w,b


def teste():
    teste1 =[1,2,3]
    teste2 =[4,5,6]
    teste3 = soma_vetorial(teste1,teste2)
    teste4 = mul_escalar(teste1,2)
    teste5 = mul_ele_vetor(teste1,teste2)

    print("soma de vetores",teste3)
    print("multiplicação por escalar", teste4)
    print("multiplica elemento a elemento entre vetores", teste5)


def main():
    X = [[1,1],[1,0],[0,1],[0,0]]
    d = [1,-1,-1,-1]
    
    # Implemente a função Adaline que deve retornar o vetor de pesos e o bias, respectivamente.
    w, bias = adaline(max_it=100, Epsilon=.0000001, alpha=.1, X=X, d=d)
    plotar(w[0],w[1],bias,"Porta lógica AND com Adaline")
    
    # Implemente a função Percepton que deve retornar o vetor de pesos e o bias, respectivamente.
    # w, bias = perceptron(max_it=100, E=1, alpha=.1, X=X, d=d)
    # plotar(w[0],w[1],bias,"Porta lógica AND com Perceptron")

if __name__ == '__main__':
    main()