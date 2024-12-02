n = int(input('Digite a quantidade de número que deseja ver da sequencia de fibonacci: '))
fi = 0
fi_antigo = 0
contador = 0
while contador < n:
    if contador == 0:
        print(fi, end='-')
        print(contador)
        contador += 1
        fi += 1
    elif contador == 1:
        print(fi, end='-')
        print(contador)
        contador += 1
    else:
        fi_antigo = fi

        print(fi,end=' fi ')
        print(contador, 'contador')
        contador += 1
        fi += fi_antigo

