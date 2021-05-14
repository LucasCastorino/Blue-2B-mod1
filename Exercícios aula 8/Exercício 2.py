'''2.	Faça um jogo da forca.
O programa terá uma lista de palavras lidas deum arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado.'''
import random


def print_forca(forca):
    print(' '.join(forca).upper())
    print('')


palavras = ['programa', 'arquivo', 'texto',
            'aleatoriamente', 'jogador', 'enforcado']
palavra = random.choice(palavras)
forca = ['_' for i in range(len(palavra))]
erros = 0
ganhou = False

while erros < 6 and not ganhou:
    print_forca(forca)
    print('Digite uma letra:')
    chute = str(input()).lower()

    if chute not in palavra:
        erros += 1
        print(f'Você errou pela {erros}a vez. Tente de novo!')
        continue

    for index, letra in enumerate(palavra):
        if letra == chute:
            forca[index] = chute

    if '_' not in forca:
        ganhou = True

if ganhou:
    print('You win!')
else:
    print('Game over!')
print_forca(forca)
