from time import sleep
print('Diga o valor do seu produto e a forma de pagamento e saberá quanto será pago ao total!')
sleep(2)
valor = float(input('Qual é o valor do seu produto? R$ '))
print('Escolha a forma de pagamento:')
print('Opção 1 - À vista no dinheiro/cheque com 10% de desconto')
print('Opção 2 - À visto no cartão com 5% de desconto')
print('Opção 3 - Em até 2x no cartão sem juros')
print('Opção 4 - Em 3x ou mais no cartão com 20% de juros')
opcao = int(input('Qual opção deseja: '))

if opcao == 1:
    print('Seu produto custa R${:.2f}, o valor total a ser pago no dinheiro/cheque com desconto de 10% será R${:.2f}'.format(valor, valor - (valor * 0.10)))
elif opcao == 2:
    print('Seu produto custa R${:.2f}, o valor total a ser pago no cartão com desconto de 5% será R${:.2f}'.format(valor, valor - (valor * 0.05)))
elif opcao ==3:
    print('Seu produto custa R${:.2f}, o valor total a ser pago em até 2x no cartão será R${:.2f}'.format(valor, valor))
elif opcao == 4:
    print('Seu produto custa R${:.2f}, o valor a ser pago pode ser parcelado em 3x ou mais no cartão com acréscimo de 20% de juros e o total a ser pago será R${:.2f}'.format(valor, (valor + (valor * 0.20))))
else:
    print('Opção inválida!')
