# Fatorial de um número com o while
print('-='*15)
print('Calculadora de Fatorial')
print('-='*15)
valor = int(input('Digite um número: '))
fatorial = 1
contador = valor
while contador > 0:
    fatorial *= contador
    print(f'{contador} * ' if contador > 1 else f'{contador} = ',end='')
    contador -= 1
print(fatorial)