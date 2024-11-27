n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
print('A sua média foi {}'.format(med))
if med < 5:
    print('REPROVADO!')
elif med < 7:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')