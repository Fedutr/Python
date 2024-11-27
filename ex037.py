print('-='*20)
print('\033[1mBase de Conversão\033[m')
print('-='*20)

num = int(input('Digite um número: '))
tipo = int(input('Conversão\nDigite 1 para binário\nDigite 2 para octal\nDigite 3 para hexadecimal: '))

print('O número digitado foi {}'.format(num))
if tipo == 1:
    print('Convertido para binário fica: {:}'.format(bin(num)))
elif tipo == 2:
    print('Convertido para octal fica: {:}'.format(oct(num)))
else:
    print('Convertido para hexadecimal fica: {:}'.format(hex(num)))