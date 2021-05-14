def pn(n):
    if n > 0:
        print('Positivo')
    elif n == 0:
        print('Neutro')
    else:
        print('Negativo')


print('Positivo ou negativo')
n = float(input('digite um numero: '))
print('Este número é ', end='')
pn(n)
