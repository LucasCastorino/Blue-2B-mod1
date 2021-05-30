# 08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com Idade) em um dicionário.
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de Contratação e o salário.
# Calcule e acrescente , além da Idade, com quantos anos a pessoa vai se aposentar.
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
from datetime import datetime
dados = {}
dados['Nome'] = input('Informe seu nome: ')
nasc = int(input('Informe o ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
if dados['Idade'] > 14:
    dados['CTPS'] = int(input('Informe o número da CTPS: '))
    if dados['CTPS'] != 0:
        dados['Contratação'] = int(input('Ano de Contratação: '))
        dados['Salário'] = int(input('Salário: R$ '))
        dados['Aposentadoria'] = dados['Idade'] + \
            ((dados['Contratação'] + 35) - datetime.now().year)
        for k, v in dados.items():
            print(f'- {k}: {v}')
else:
    print('Idade menor que a necessária para começar a trabalhar.')
