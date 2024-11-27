print('-='*20)
print('\033[1mBase de Conversão\033[m')
print('-='*20)

num = int(input('Digite um número: '))
print('''Conversão
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal''')
tipo = int(input('Sua opção: '))
print('O número digitado foi {}'.format(num))
if tipo == 1:
    print('Convertido para binário fica: {}'.format(bin(num)[2:]))
elif tipo == 2:
    print('Convertido para octal fica: {}'.format(oct(num)[2:]))
elif tipo == 3:
    print('Convertido para hexadecimal fica: {}'.format(hex(num)[2:]))
else:
    print('Opção Invalida')