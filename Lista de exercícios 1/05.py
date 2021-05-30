# 05 - Refatore o exercício 2, para que uma função receba a frase,
# faça todo o tratamento necessário e retorne o resultado.
# Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.


def remove_vogal(frase):
    count = 0
    for vogal in frase:
        if vogal in 'aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûÍÌÎíìî':
            count = count+1
            frase = frase.replace(vogal, "")
    print("Número de vogais:", count)
    print(frase)


remove_vogal(input('Digite uma frase: '))
