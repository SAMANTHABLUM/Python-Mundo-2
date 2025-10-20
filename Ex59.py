print('Você irá digitar DOIS NUMEROS e logo abaixo terá opções do que deseja fazer com eles.')
num_1 = int(input('Digite o primeiro valor: '))
num_2 = int(input('Digite o segundo valor: '))
print('Digite [1] para SOMAR')
print('Digite [2] para MULTIPLICAR')
print('Digite [3] para saber o MAIOR')
print('Digite [4] para NOVOS numeros')
print('Digite [5] para SAIR')
opcao = 0
while opcao != 5:
    opcao = int(input('Qual opção deseja? '))
    if opcao == 1:
        print('A soma de {} e {} é {}.'.format(num_1, num_2,(num_1 + num_2)))
    elif opcao == 2:
        print('A multiplicação de {} e {} é {}.'.format(num_1, num_2, (num_1 * num_2)))
    elif opcao == 3:
        if num_1 > num_2:
            print('O numero {} é MAIOR que o {}'.format(num_1, num_2))
        else:
            print('O numero {} é MAIOR que o {}'.format(num_2, num_1))
    elif opcao == 4:
        num_1 = int(input('Digite o primeiro novo valor: '))
        num_2 = int(input('Digite o segundo novo valor: '))
    else:
        print('Opção inválida, tente novamente!')
print('Você SAIU!')