from datetime import datetime #importação da biblioteca para ano usar datetime.now().year
print('Vamos falar sobre ALISTAMENTO MILITAR')
nasc = int(input('Qual foi o ano do seu nascimento? '))
year = datetime.now().year
idade = year - nasc
tempo = abs(idade - 18) # usada condição abs() para nao ficar negativo o tempo na primeira opção
if idade < 18:
    print('Você ainda vai se alistar, falta {} anos.'.format(tempo))
elif idade == 18:
    print('Está na hora de se alistar')
else:
    print('Já passou {} anos do tempo de se alistar'.format(tempo))