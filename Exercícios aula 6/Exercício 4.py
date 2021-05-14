def salario(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas*taxa
    else:
        hora_extra = horas - 40
        salario = 40*taxa+(hora_extra*(1.5*taxa))
    return salario


str_horas = input('Digite as horas: ')
str_taxa = input('Digite a taxa: ')
total_salario = salario(str_horas, str_taxa)
print('O valor de seus rendimentos é R$', total_salario)
