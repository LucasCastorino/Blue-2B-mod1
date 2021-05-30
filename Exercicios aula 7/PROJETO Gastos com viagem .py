# PROJETO: Gastos com viagem - Escrever uma aplicação utilizando funções que calcule os gastos com passagem, hospedagem, aluguel de carro e gastos extras de uma viagem para uma determinada cidade.
# Hospedagem
# 1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.

def custo_hotel(noites):
    noite = 140.00
    noites = int(input('Digite a quantidade de noites:'))
    noites = noites * noite
    return noites

# Passagem
# 2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que passagem para:
# - São Paulo custa R$ 312,00;
# - Porto Alegre custa R$ 447,00;
# - Recife custa R$ 831,00;
# - Manaus custa R$ 986,00.


def custo_aviao(cidade):
    print('Cidades disponíveis para viagem:')
    print('1-São Paulo\n2-Porto Alegre\n 3-Recife\n 4-Manaus\n')
    cidade = int(input('Digite o número respectivo a cidade:'))
    while cidade != 1 or cidade != 2 or cidade != 3 or cidade != 4:
        cidade = int(input('Digite o número respectivo a cidade:'))
    if cidade == 1:
        passagem = 312.00
        print('São Paulo custa R$ 312,00')
    elif cidade == 2:
        passagem = 312.00
        print('Porto Alegre custa R$ 447,00')
    elif cidade == 3:
        passagem = 831.00
        print('Recife custa R$ 831,00')
    elif cidade == 4:
        passagem = 986.00
        print('Manaus custa R$ 986,00')
    return passagem

# Aluguel de Carro
# 3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
# - Calcule o custo do aluguel do carro sendo que:
# - A cada dia o carro custa R$ 40,00;
# - Alugando 7 dias ou +: R$ 50,00 de desconto;
# - Alugando 3 dias ou +: R$ 20,00 de desconto;
# - Você pode receber apenas um desconto;
# - Retorne o custo.


def custo_carro(dias_carro):
    dias_carro = int(input('Digite a quantidade de dias a alugar: '))
    if dias_carro < 3:
        aluguel_carro = dias_carro * 40.00
    elif dias_carro < 7:
        aluguel_carro = (dias_carro*40) - 20
    else:
        aluguel_carro = (dias_carro*40) - 50

    return ('Aluguel de', dias_carro, 'dias, custa:', aluguel_carro)

# Cálculo Total
# 4 - Agora com essas três funções criadas, declare uma função que receba a cidade
# e quantidade de dias e retorne o custo total da viagem.
# - Reutilize as funções já criadas.
# - Exiba o total da viagem chamando apenas a nova função declarada!


custo_hotel(noites)
custo_aviao(cidade)
custo_carro(dias_carro)


# def calculo_total(total,):
#     total = noites +


# Gastos Extras
# 5 - Modifique essa nova função criada e adicione um terceiro argumento:
# 'gastos_extras' e some esse valor ao total da viagem.
# Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastandoR$ 800,00 adicionais.
