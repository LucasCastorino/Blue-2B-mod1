'''Escreva uma função que recebe dois números (a e b) como parâmetroe retorna True
caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.'''


def menor(a, b):
    limite = 10
    if (a + b) > limite:
        print('True:')
    else:
        print('False:')


a = float(input('Digite o primeiro numero: '))
b = float(input("Digite o segunto número: "))
menor(a, b)
