def somaImposto(taxaImposto, custo):
    return (1 + taxaImposto/100)*custo


t = float(input('Digite a taxa de imposto: '))
c = float(input('Digite o custo: '))
print('Valor do imposto:', somaImposto(t, c))
