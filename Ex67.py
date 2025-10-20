while True:
    n = int(input('Digite o número de qual tabuada deseja saber: '))
    if n < 0:
        print('Encerrado')
        break
    for c in range (0, 11):
        print(f'{n} X {c} : {n*c}')