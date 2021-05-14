valor_pao = float(input("Digite o valor do pão").replace(',', '.'))
print("Preço do pão: R$", valor_pao)
print("Panificadora Pão de Ontem - Tabela de preços")
for i in range(1, 11):
    print("{} - R$ {:.2f}".format(i, valor_pao*i))
