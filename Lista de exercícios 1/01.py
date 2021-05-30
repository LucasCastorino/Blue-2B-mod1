# 01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
# A soma deles;
# A multiplicação entre eles;
# A divisão inteira deles;
# Mostre na tela qual é o maior;
# Verifique se o resultado da soma é par ou impar e mostre na tela;
# Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela.
# Se não, mostre que a multiplicação não foi maior que 40.

num1 = float(input('Digite o primeiro número: ').replace(',', '.'))
num2 = float(input('Digite o segundo número: ').replace(',', '.'))
soma = num1 + num2
mult = num1 * num2
print(f'A soma dos números é: {soma}.')
print(f'A Multiplicação dos dois números é {mult}.')
if num1 > num2:
    print(f'{num1} é maior que {num2}.')
elif num1 == num2:
    print(f'Os números são iguais.')
else:
    print(f'{num2} é maior que {num1}.')
if num2 != 0:
    div = num1 // num2
    print(f'A divisão inteira dos números é: {div}.')
    if num1 % num2 == 0:
        print(f'O resultado da soma é {soma} e é par.')
    else:
        print(f'O resultado da soma é {soma} e é ímpar.')
    if mult > 40:
        resultado = mult/div
        print(
            f'O resultado da multiplicação dividido pelo resultado da divisão inteira é: {resultado}.')
    else:
        print('O resultado da multiplicação é menor que 40.')
else:
    print('Impossível dividir por zero.')
