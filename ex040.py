n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1,n2, med))
if med < 5:
    print('REPROVADO!')
elif med < 7:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')