'''
Exercício Treino 1 - Escreva uma função que recebe dois parâmetros (números) 
e imprime o menor dos dois.Se eles forem iguais, imprima que são valores idênticos.
'''


def menor(a, b):
    if a > b:
        print('O menor valor é:', b)
    elif a == b:
        print('Os valotes são idênticos.')
    else:
        print('O menor valor é:', a)


a = float(input('Digite o primeiro numero: '))
b = float(input("Digite o segunto número: "))
menor(a, b)
