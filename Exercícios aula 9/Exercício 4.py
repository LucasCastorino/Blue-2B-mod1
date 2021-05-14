nomes = []

a = input('Digite um nome para acrescentar à lista ou 0 para sair: ').lower()
while a != '0':
    nomes.append(a.lower())
    a = input('Digite um nome para acrescentar à lista ou 0 para sair: ').lower()

nome = input("Digite um nome a ser buscado na lista: ").lower()
if nome in nomes:
    print("O nome está na lista")
else:
    print("O nome não está na lista")
