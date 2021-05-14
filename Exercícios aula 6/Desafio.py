'''Data com mês por extenso. 
Construa uma função que receba uma data no formato DD/MM/AAAAe devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida. 
Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.'''


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
        # Mês por extenso:
        if mes == 1:
            mes = 'Janeiro'
        elif mes == 2:
            mes = 'Fevereiro'
        elif mes == 3:
            mes = "Março"
        elif mes == 4:
            mes = "Abril"
        elif mes == 5:
            mes = "Maio"
        elif mes == 6:
            mes = "Junho"
        elif mes == 7:
            mes = "Julho"
        elif mes == 8:
            mes = "Agosto"
        elif mes == 9:
            mes = "Setembro"
        elif mes == 10:
            mes = "Outubro"
        elif mes == 11:
            mes = "Novembro"
        else:
            mes = "Dezembro"

        print(dia, 'de', mes, 'de', ano)
    else:
        print('NULL')


data = input("Digite a data DD/MM/AAAA\n")
data_valida(data)
