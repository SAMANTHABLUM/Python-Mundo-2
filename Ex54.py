from datetime import datetime #importação da biblioteca para ano usar datetime.now().year
year = datetime.now().year
maior = 0
menor = 0
for c in range (0, 7):
    nasc = int(input('Digite o ano do seu nascimento: '))
    idade = year - nasc
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} pessoas são maiores de idade'.format(maior))
print('{} pessoas são MENORES de idade'.format(menor))