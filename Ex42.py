from time import sleep
print('DESAFIO DOS TRIANGULOS')
sleep(1)
print('O triangulo será formado? Depende dos valores e se sim, direi o TIPO!')
sleep(1)
r1 = int(input('Digite o primeiro valor: '))
r2 = int(input('Digite o segundo valor: '))
r3 = int(input('Digite o terceiro valor: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1: # Se for um triângulo, continue a análise do tipo
    print('É um triangulo')
    if r1 == r2 and r2 == r3: # esse if precisar estar "dentro" do primeiro if quando se trata do primeiro if ser verdadeiro
        print('E ele é do tipo EQUILÁTERO')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('E ele é do tipo ISOSCELES')
    else:
        print('E ele é do tipo ESCALENO')
else:
    print('Valores não formam nenhum triangulo!')