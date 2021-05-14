'''Escreva uma função que, dado um número nota representando a nota de um estudante,
converte o valor de nota para um conceito (A, B, C, D, E e F).'''


def conceito(nota):
    nota = float(nota)
    if nota <= 4:
        print('F')
    elif nota <= 7:
        print('D')
    elif nota <= 8:
        print('C')
    elif nota <= 9:
        print('B')
    else:
        print('A')


nota = float(input('Digite o valor da nota: '))
while nota < 0 or nota > 10:
    print('Nota fora dos limites')
    nota = float(input('Digite novamente: '))
conceito(nota)
