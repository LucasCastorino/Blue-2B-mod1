'''7.	Escreva uma função que recebe dois parâmetros e imprime o menor dos dois.
Se eles forem iguais, imprima que eles são iguais.'''


def menor(a, b):
    if a > b:
        print('O menor valor é:', b)
    else:
        print('O menor valor é:', a)


a = float(input('Digite o primeiro numero: '))
b = float(input("Digite o segunto número: "))
menor(a, b)
