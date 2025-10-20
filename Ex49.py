n = int(input('Digite o número de qual tabuada deseja saber: '))
for c in range (0, 11):
    print('{} X {} : {}'.format(n,c,n*c))