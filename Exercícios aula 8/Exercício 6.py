'''Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.'''

frase = input('Digite uma frase: ')
count = 0
for vogal in frase:
    if vogal in 'aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûÍÌÎíìî':
        frase = frase.replace(vogal, "")

print(frase)
