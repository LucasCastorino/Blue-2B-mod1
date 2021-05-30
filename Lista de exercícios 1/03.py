# 03 - Utilizando estruturas de repetição com teste lógico,
# faça um programa que peça uma senha para iniciar seu processamento,
# só deixe o usuário continuar se a senha estiver correta,
# após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação,
# onde o computador vai “pensar” em um número inteiro entre 0 e 20.
# O jogador vai tentar adivinhar qual número foi escolhido até acertar,
# a cada palpite do usuário diga a ele se o número escolhido pelo computador
# é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

from random import randint
senha = 123
opc = 0
entrada = int(input("Digite a senha numérica: "))
while entrada != senha:
    print("Senha incorreta")
    entrada = int(input("Digite a senha novamente: "))
    opc += 1
    if opc == 3:
        print("Tentativas Esgotadas")
        quit()
print('Senha correta.\nBem vindo ao jogo de advinhação!')

adv = randint(0, 20)
num = int(input('Para jogar tente adivinhar um número inteiro de 0 a 20: '))
while num != adv:
    if num > adv:
        print('Número maior que o palpite!')
        num = int(input('Tente novamente: '))
    elif num < adv:
        print('Número menor que o palpite!')
        num = int(input('Tente novamente: '))
print('Você acertou!')
