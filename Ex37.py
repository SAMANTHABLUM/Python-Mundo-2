num = int(input('Digite um numero: '))
print('Digite 1 - para reverter em BINÁRIO')
print('Digite 2 - para reverter em OCTAL')
print('Digite 3 - para reverter em HEXADECIMAL')
opcao = int(input('Qual opção deseja? '))
if opcao == 1:
    print('O numero {} em BINÁRIO fica {}'.format(num, bin(num)))
elif opcao ==2:
    print('O numero {} em OCTAL fica {}'.format(num, oct(num)))
elif opcao == 3:
    print('O numero {} em HEXADECIMAL fica {}'.format(num, hex(num)))
else:
    print('Opção inválida')