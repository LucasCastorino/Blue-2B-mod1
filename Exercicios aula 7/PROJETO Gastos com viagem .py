def custo_hotel(noites):
    return noites * 140


def custo_aviao(cidade):
    passagem = 0
    if cidade == 'são paulo' or cidade == 'sao paulo':
        passagem = 312.00
    elif cidade == 'porto alegre':
        passagem = 312.00
    elif cidade == 'recife':
        passagem = 831.00
    elif cidade == 'manaus':
        passagem = 986.00
    else:
        print('Não temos passagem para esta cidade.')
    return passagem


def custo_carro(dias_carro):
    if dias_carro < 3:
        aluguel_carro = dias_carro * 40.00
    elif dias_carro < 7:
        aluguel_carro = (dias_carro*40) - 20
    else:
        aluguel_carro = (dias_carro*40) - 50
    return aluguel_carro


def calculo_total(custo_hospedagem, passagem, aluguel_carro, gastos_extras):
    total_hotel = custo_hotel(custo_hospedagem)
    total_passagem = custo_aviao(passagem)
    total_carro = custo_carro(aluguel_carro)
    custo_total = total_hotel + total_passagem + total_carro + gastos_extras
    print(
        f'O custo da uma viagem de {noites} dias para {cidade} gastando R$ {gastos_extras} adicionais é {custo_total}'
    )
    return custo_total


noites = int(input('Quantas noites ficará hospedado? '))
print('Cidades disponíveis para viagem:\nSão Paulo\nPorto Alegre\nRecife\nManaus')
cidade = input('Digite a cidade destino: ')
carro = int(input('Por quantos dias alugará o carro? '))
gastos_extras = float(input('Gastos extras: '))
total = calculo_total(noites, cidade, carro, gastos_extras)
