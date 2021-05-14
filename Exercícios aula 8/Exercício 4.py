'''4.	Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), 
conte quantas vezes aparece uma vogal.'''

frase = input('Digite uma frase: ')
count = 0
for vogal in frase:
    if vogal in 'aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûÍÌÎíìî':
        count = count+1

print("Número de vogais:", count)
