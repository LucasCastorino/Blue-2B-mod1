# Um professor, muito legal, fez 3 provas durante um semestre,
# mas só vai levar em conta as duas notas mais altas para calcular a média.
# Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas,
# a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

def notas():
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))

    maior = nota1
    if (nota2 > maior):
        maior = nota2
    if (nota3 > maior):
        maior = nota3

    menor = nota1
    if (nota2 < menor):
        menor = nota2
    if (nota3 < menor):
        menor = nota3

    maior2 = 0
    if maior > nota1 and menor < nota1:
        maior2 = nota1
    if maior > nota2 and menor < nota2:
        maior2 = nota2
    if maior > nota3 and menor < nota3:
        maior2 = nota3

    print(f'Maior nota: {maior},Segunda maior: {maior2},Menor nota:{menor}')
    media3 = (maior + maior2 + menor)/3
    media2 = (maior + maior2)/2

    return 'Média com 3 notas:', media3, 'Média com 2 notas:', media2


print(notas())
