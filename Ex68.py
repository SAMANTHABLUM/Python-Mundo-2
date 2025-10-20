import random # importado biblioteca random que serve para sortear algo aleatorio
from time import sleep
c = 0
print('-=-'*10)
sleep(1)
print ('VAMOR JOGAR PAR ou IMPAR!!!')
sleep(1)
print('-=-'*10)
sleep(1)
while True:
   computador = random.randint(0, 10)
   jogador = int(input('Qual é o numero que escolheu? '))
   opcao = str(input('Quer IMPAR ou PAR? [I/P]: ')).strip().lower()[0]
   total = computador + jogador
   print(f'Você jogou {jogador} e o computador jogou {computador}. Total = {total}')
   if total % 2 == 0: #PAR
       if opcao == 'p':
           print('Você ganhou, vamos jogar de novo!')
           c += 1
       else:
           print(f'Game Over, você perdeu com {c} tentativas')
           break
   else: #IMPAR
       if opcao == 'i':
           print('Você ganhou, vamos jogar de novo!')
           c += 1
       else:
           print(f'Game Over, você perdeu com {c} tentativas')
           break
