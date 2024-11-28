numero = int(input('Digite um número: '))
divisores = 0
for c in range(1, numero+1):
    if numero % c == 0:
        divisores += 1
if divisores == 2:
    print('O número {} é primo!'.format(numero))
else:
    print('O número {} não é primo!'.format(numero))