from time import sleep
print('Vamos descobrir agora quais são os numeros ímpares multiplos de 3 no intervalo de 1 até 500.')
sleep(1)
soma = 0
for c in range (0, 501):
    if c % 3 == 0:
        if c % 2 != 0:
            soma = soma + c
print('A soma é {}'.format(soma))