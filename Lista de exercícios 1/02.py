# 02 - Utilizando estruturas de repetição com variável de controle,
# faça um programa que receba uma string com uma frase informada pelo usuário
# e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela,
# depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = input('Digite uma frase: ')
count = 0
for vogal in frase:
    if vogal in 'aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûÍÌÎíìî':
        count = count+1
        frase = frase.replace(vogal, "")
print("Número de vogais:", count)
print(frase)
