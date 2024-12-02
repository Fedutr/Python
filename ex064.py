contador = 0
n= 0
soma = 0
while n != 999:
    n = int(input('Digite um valor: '))
    contador += 1
    soma += n
print(f'Você digitou {contador-1} números')
print(f'A soma dos número digitados é igual a {soma-999}')