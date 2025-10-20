print('Me informe dois valores e direi qual é o maior!')
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
if num1 > num2:
    print('O primeiro numero informado {} é MAIOR que o segundo numero informado {}.'.format(num1, num2))
elif num2 > num1:
    print('O segundo numero informado {} é MAIOR que o primeiro numero informado {}.'.format(num2, num1))
elif num1 == num2:
    print('Os dois numeros informado são iguais!')