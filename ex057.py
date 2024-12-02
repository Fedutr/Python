sexo = str(input('Você é do sexo Masculino [M] ou Feminino [F]? ')).strip().upper()[0] #Pegando apenas a primeira letra em maiusculo
while sexo not in  'MmFf':
        print('Opções Invalida')
print(f'Sexo {sexo} registrado com sucesso.')
