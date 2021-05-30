# 04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA
# e devolva uma string no formato D de mesPorExtenso de AAAA.
# Valide a data e retorne NULL caso a data seja inválida.

def data_valida(data):
    valida = False

    # faz o split e transforma em números
    dia, mes, ano = map(int, data.split('/'))

    # Meses com 31 dias
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or
            mes == 8 or mes == 10 or mes == 12):
        if(dia <= 31):
            valida = True
    # Meses com 30 dias
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if(dia <= 30):
            valida = True
    elif mes == 2:
        # Testa se é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if(dia <= 29):
                valida = True
        elif(dia <= 28):
            valida = True
    # Mês por extenso:
    if(valida):
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        print(f'{dia} de {meses[mes-1]} de {ano}.')
    else:
        print('NULL')


data = input("Digite a data DD/MM/AAAA\n")
data_valida(data)
