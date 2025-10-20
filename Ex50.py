print('Você precisa digitar 6 numeros e eu te darei a resposta com a soma dos numero PARES!')
soma = 0
for c in range(0,6):
    n = int(input('Digite 6 numero: '))
    if n % 2 ==0:
        soma = soma + n
print('A somatoria dos numeros PARES É {}.'.format(soma))