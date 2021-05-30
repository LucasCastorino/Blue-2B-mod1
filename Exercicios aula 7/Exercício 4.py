# Crie um programa que tenha uma função chamada voto ()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
# Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.

from datetime import date


def voto(idade):
    ano_atual = date.today().year - idade
    print(date.today().year)
    print("Sua idade é: ", ano_atual)
    if 16 <= ano_atual < 18:
        return "OPICIONAL"
    if ano_atual >= 18:
        return 'OBRIGARTÓRIO'
    else:
        return 'NEGADO'


nasc = int(input("Digite o ano do seu nascimento: "))
print(voto(nasc))
