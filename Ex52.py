n = int(input('Digite um numero: '))
if n <= 1:
    print('Não é um numero PRIMO')
else:
    divisores = 0
    for c in range(1, n+1):
        if n % c == 0:
            divisores = divisores + 1
    if divisores == 2:
        print('É um numero PRIMO!!!')
    else:
        print('Não é um numero PRIMO')