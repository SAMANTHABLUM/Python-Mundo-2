from datetime import datetime
print('A Confereração Nacional de Natação precisa saber qual é sua categoria!')
nasc = int(input('Qual o ano do seu nascimento? '))
year = datetime.now().year # sempre que precisar do ano usar datetime.now().year
idade = year - nasc
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <=19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
else:
    print('MASTER')