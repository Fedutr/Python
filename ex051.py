primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
for c in range(10):
    termo = primeiro_termo + c * razao
    print(termo, end=' ')