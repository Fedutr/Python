contador = 0
soma = 0
maior = menor = 0
seguir = 'S'
while seguir == 'S':
    valor = int(input('Digite um valor: '))
    soma+= valor
    seguir = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if contador == 0:
        maior = valor
        menor = valor
    elif valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    contador += 1

media = soma / contador
print(f'O maior valor foi {maior}\nO menor valor foi {menor}\nA média dos valores digitados foi {media:.2f}')