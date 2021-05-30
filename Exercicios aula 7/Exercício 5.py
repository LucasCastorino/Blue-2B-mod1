# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
    resultado = print(f'{nome} fez {gols} gol(s)! ')
    return resultado


ficha('Lucas', 1)
