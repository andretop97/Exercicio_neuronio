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


def multiplicacao_escalar(Vetor1, const):
    vetor_resultante = [0]*len(Vetor1)
    for i in range(len(Vetor1)):
        vetor_resultante[i] = Vetor1[i]*const
    return vetor_resultante


def mul_ele_vetor(Vetor1,Vetor2):
    vetor_resultante = [0]*len(Vetor1)
    for i in range(len(Vetor1)):
        vetor_resultante[i] = Vetor1[i] * Vetor2[i]
    return vetor_resultante
