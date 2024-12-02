primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 10
while contador > 0:
    print(primeiro_termo, end=' ')
    primeiro_termo += razao
    contador -= 1