primeiro = int(input('Qual será o primeiro termo da PA? '))
razao = int(input('Qual será a razão da PA? '))
decimo = primeiro + (10- 1) * razao
for c in range (primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')