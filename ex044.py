preço = float(input('Digite o preço do produto: R$'))
print('Condições de Pagamento')
print('[ 1 ] À vista dinheiro/cheque: 10% de desconto')
print('[ 2 ] À vista no cartão: 5% de desconto')
print('[ 3 ] Em até 2x no cartão: preço normal')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')
escolha = int(input('Qual é a opção: '))
if escolha == 1:
    preçon = preço * 0.9
    print('Você recebeu um desconto de 10%, o preço do seu produto que era R${:.2f}, ficou R${:.2f}'.format(preço, preçon))
elif escolha == 2:
    preçon = preço * 0.95
    print('Você recebeu um desconto de 5%, o preço do seu produto que era R${:.2f}, ficou R${:.2f}'.format(preço, preçon))
elif escolha == 3:
    print('Você não receberá desconto, o preço do seu produto será R${:.2f}'.format(preço))
elif escolha == 4:
    preçon = preço * 1.2
    parcelas = int(input('Quantas parcelas? '))
    preçoParcela = preçon / parcelas
    print('Sua compra será parcelada em {} vezes de {} COM JUROS'.format(parcelas, preçoParcela))
    print('Você terá que pagar um juros de 20%, o preço do seu produto que era R${:.2f}, ficou R${:.2f}'.format(preço, preçon))
else:
    print('Número não identificado')

